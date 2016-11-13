#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    kanban todo <name>...
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
    intro = '\n\t++++++++++++++++++++++++++++++++++++++++++++++\n\n' \
            '\tWelcome to KanBan Console Application!\n\n' \
            '\tAdd, organize and view your tasks\n\n' \
            '\tThe Commands For Any Action Are Listed Below\n\n' \
            '\t---------------------------------------------\n'\
            '\ttodo task_name : Create A todo Task \n' \
            '\tdoing task_id  : Start Doing Task \n' \
            '\tdone task_id   : Mark Task Done \n' \
            '\tlist todo      : View Task You Supposed To Do\n' \
            '\tlist doing     : View Task You Are Doing \n' \
            '\tlist done      : View Task You Have Finished\n' \
            '\tlist all       : View All Your Tasks In All Sections\n' \
            '\tquit           : To Exit\n' \
            '\t---------------------------------------------\n\n' \
            '\t+++++++++++++++++++++++++++++++++++++++++++++++++\n'

    prompt = '(KanBan Console) '
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

    def todo_tasks(self):
        self.kanban.list_todo()

    # start commands here
    @docopt_cmd
    def do_todo(self, args):
        """Create a todo task. For example todo email Kipngotie at 2pm
        Usage: todo <name>..."""
        self.create(args["<name>"])

    @docopt_cmd
    def do_done(self, args):
        """Finish a task. For example: done 52
        Usage: done <task_id>"""
        self.done(args["<task_id>"])

    @docopt_cmd
    def do_doing(self, args):
        """ Start doing a task. For example: doing 52
        Usage: doing <task_id>"""
        self.doing(args["<task_id>"])

    @docopt_cmd
    def do_list(self, args):
        """List task as per their section.
           list all, list done, list doing list todo
        Usage: list <command> """
        if args['<command>'] == 'all':
            self.tasks()
        elif args['<command>'] == 'doing':
            self.doing_tasks()
        elif args['<command>'] == 'done':
            self.done_tasks()
        elif args['<command>'] == 'todo':
            self.todo_tasks()
        else:
            print('Invalid Command! use <all> or <done> or <doing>\n eg list all.')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('\nBye Bye! See you soon!\n')
        exit()

# interactive mode
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
