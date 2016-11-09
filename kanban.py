#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    kanban todo <name>
    kanban doing <task_id>
    kanban done <task_id>
    kanban list <command>
    kanban (-i | --interactive)
    kanban (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from model import KanBan


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command! Try Another one.')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to KanBan! We organize your tasks!' \
        + ' (type help for a list of commands.)'
    prompt = '(KanBan) '
    file = None
    kanban = KanBan()

    # start functions here
    def create(self, name):
        self.kanban.create_task(name)

    def doing(self, task_id):
        self.kanban.doing_task(task_id)

    def done(self, task_id):
        self.kanban.done_task(task_id)

    def tasks(self):
        self.kanban.list_all()

    def doing_tasks(self):
        self.kanban.list_doing()

    def done_tasks(self):
        self.kanban.list_done()

    # start commands here
    @docopt_cmd
    def do_todo(self, args):
        """Usage: todo <name>"""
        self.create(args["<name>"])

    @docopt_cmd
    def do_done(self, args):
        """Usage: done <task_id>"""
        self.done(int(args["<task_id>"]))

    @docopt_cmd
    def do_doing(self, args):
        """Usage: doing <task_id>"""
        self.doing(int(args["<task_id>"]))

    @docopt_cmd
    def do_list(self, args):
        """Usage: list <command> """
        if args['<command>'] == 'all':
            self.tasks()
        elif args['<command>'] == 'doing':
            self.doing_tasks()
        elif args['<command>'] == 'done':
            self.done_tasks()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()

# interactive mode
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
