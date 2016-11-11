import sqlite3
from datetime import datetime
from tabulate import tabulate

"""KanBan Class For Creating, Moving and Displaying Tasks"""

class KanBan(object):
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.start = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.create_table()

    # Creates the task table in the kanBanApp database.
    def create_table(self):
        table = 'CREATE TABLE IF NOT EXISTS task(' \
                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                'title TEXT,' \
                'status TEXT, ' \
                'start_on DATETIME, ' \
                'end_on DATETIME );'
        self.cursor.execute(table)

    # Creates a new task and displays it
    def create_task(self, name):
        self.name = name
        self.task_name = ' '.join(self.name)
        self.section = 'todo'
        insert_query = 'INSERT INTO task(title, status) VALUES(?, ?)'
        self.cursor.execute(insert_query, (self.task_name, self.section))

        # get the created task
        print("\nTask added!\n")

        self.cursor.execute("SELECT MAX(id), title, status, start_on, end_on FROM task")

        task = self.cursor.fetchall()

        for row in task:

            task_list = [row[0], row[1], row[2], row[3], row[4]]

        print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                           numalign="center"))
        self.conn.commit()

        print('\n')

    # moves a task from to do section to doing section
    def doing_task(self, task_id):
        self.move_task(task_id, 'doing')

    # moves a task from doing section to done section
    def done_task(self, task_id):
        self.move_task(task_id, 'done')

    # Displays All the Tasks
    def list_all(self):
        section = 'all'
        self.list_section(section)

    # Displays all the tasks in the doing section
    def list_doing(self):
        section = 'doing'
        self.list_section(section)

    def list_todo(self):
        section = 'todo'
        self.list_section(section)

    # Displays all the completed tasks
    def list_done(self):
        section = 'done'
        self.list_section(section)

    # retrieves and display tasks depending on the section
    def list_section(self, section):
        self.section = section

        # done section tasks
        if self.section == 'done':
            query_section = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'done'"
            self.cursor.execute(query_section)
            records = self.cursor.fetchall()
            if not records:
                print("\nYou have not finished any task yet.\n")
            else:
                done_list = []
                print('\nThese Are The Tasks You Have Completed With Time Taken\n')
                for row in records:
                    start = datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
                    stop = datetime.strptime(str(row[4]), '%Y-%m-%d %H:%M')
                    start_time, stop_time = start.strftime('%H:%M').split(':'), stop.strftime('%H:%M').split(':')
                    hours = int(stop_time[0]) - int(start_time[0])
                    minutes = int(stop_time[1]) - int(start_time[1])
                    tasks_duration = [row[0], row[1], row[2], hours, minutes]
                    done_list.append(tasks_duration)

                print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
                               numalign="center"))
                print('\n')

        # done section tasks
        elif self.section == 'doing':
            query_section = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'doing'"

            self.cursor.execute(query_section)
            records = self.cursor.fetchall()
            if not records:
                print("\nYou have not finished any task yet.\n")
            else:
                done_list = []
                print('\nThese Are The Tasks You Have Completed With Time Taken\n')
                for row in records:
                    stop = datetime.strptime(self.start, '%Y-%m-%d %H:%M')
                    start = datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
                    start_time, stop_time = start.strftime('%H:%M').split(':'), stop.strftime('%H:%M').split(':')
                    hours = int(stop_time[0]) - int(start_time[0])
                    minutes = int(stop_time[1]) - int(start_time[1])
                    tasks_duration = [row[0], row[1], row[2], hours, minutes]
                    done_list.append(tasks_duration)

                print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
                               numalign="center"))
                print('\n')

        # done section tasks
        elif self.section == 'all':
            query_section = "SELECT * FROM task"
            self.cursor.execute(query_section)
            records = self.cursor.fetchall()
            if not records:
                print("\nYou have not finished any task yet.\n")
            else:
                done_list = []
                print('\nThese Are The Tasks You Have Completed With Time Taken\n')
                for row in records:
                    tasks_duration = [row[0], row[1], row[2], row[3], row[4]]
                    done_list.append(tasks_duration)

                print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Start Time", "Stop Time"],
                               numalign="center"))
                print('\n')
            # done section tasks
        elif self.section == 'todo':
            query_section = "SELECT * FROM task WHERE status = 'todo'"
            self.cursor.execute(query_section)
            records = self.cursor.fetchall()
            if not records:
                print("\nYou have not added any task yet.\n")
            else:
                done_list = []
                print('\nThese Are the tasks You are supposed to do\n')
                for row in records:
                    tasks_duration = [row[0], row[1], row[2], row[3], row[4]]
                    done_list.append(tasks_duration)

                print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Start Time", "Stop Time"],
                               numalign="center"))
                print('\n')

    # Move a task from one section to another
    def move_task(self, task_id, section):
        self.task_id = task_id
        self.section = section

        # check first if the task exits
        check = "SELECT * FROM task WHERE id = ?"
        self.cursor.execute(check, (self.task_id,))
        data = self.cursor.fetchone()

        if data is None:
            print('Sorry the task does not exits')
        else:
            # check task section if to do or doing
            # print(task_curent_section) <debug here...>

            task_current_section = data[2]  # the current section of the task
            if task_current_section == 'todo' and self.section == 'done':
                print('\nSorry! You have not Started doing that Task\n')

            elif task_current_section == 'done' and (self.section == 'done' or self.section == 'doing'):
                print('\nHey! You have Finished doing that Task\n')

            elif task_current_section == 'doing' and self.section == 'doing':
                print('\nHey! You are currently doing that Task\n')

            elif (task_current_section == 'todo' and self.section == 'doing') \
                    or (task_current_section == 'doing' and self.section == 'done'):

                # if the task is in to do section move it to doing section only
                if task_current_section == 'todo':
                    move_task = "UPDATE task SET status = ?, start_on = ? WHERE id = ?"
                    self.cursor.execute(move_task, (self.section, self.start, self.task_id))
                    self.cursor.execute("SELECT * FROM task WHERE id = ?", (self.task_id,))
                    print("\nGreat! You have started doing the Following Task\n")
                    started_task = self.cursor.fetchall()
                    for row in started_task:

                        task_list = [row[0], row[1], row[2], row[3], row[4]]

                    print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                                   numalign="center"))
                    print('\n')
                    self.conn.commit()

                # if the task is in doing section move it to done section only
                elif task_current_section == 'doing':
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                    # move the task to the appropriate section
                    move_task = "UPDATE task SET status = ?, end_on = ? WHERE id = ?"
                    done_cursor = self.cursor.execute(move_task, (self.section, current_time, self.task_id))
                    self.cursor.execute("SELECT * FROM task WHERE id = ?", (self.task_id,))
                    print("\nGreat! You have finished the Following Task\n")
                    task = done_cursor.fetchall()
                    for row in task:
                        task_list = [row[0], row[1], row[2], row[3], row[4]]

                    print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                                   numalign="center"))
                    print('\n')

                    self.conn.commit()
            else:
                print('Invalid section')
