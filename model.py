import sqlite3
from datetime import datetime
from tabulate import tabulate


class KanBan(object):
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.start = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Create database called tasks if not created

    def create_table(self):
        table = 'CREATE TABLE IF NOT EXITS task(' \
                'id INTEGER PRIMARY KEY AUTO INCREMENT,' \
                'title TEXT,' \
                'status TEXT, ' \
                'start_on DATETIME, ' \
                'end_on DATETIME );'
        self.cursor.execute(table)

    def create_task(self, title):
        self.title = title
        self.task_name = ' '.join(self.title)
        self.status = 'todo'
        insert_query = 'INSERT INTO task(title, status) VALUES(?, ?)'
        self.cursor.execute(insert_query, (self.task_name, self.status))

        # get the created task
        print("\nTask added!\n")

        self.cursor.execute("SELECT MAX(id), title, status, start_on, end_on FROM task")

        task = self.cursor.fetchall()

        for row in task:

            task_list = [row[0], row[1], row[2], row[3], row[4]]

        print(tabulate([task_list], headers=["Task Id", "Task Name", "Status", "Section", "Finish Time"],
                           numalign="center"))
        self.conn.commit()

        print('\n')

    def doing_task(self, task_id):

        self.move_task(task_id, 'doing')

    def done_task(self, task_id):

        self.move_task(task_id, 'done')

    def list_all(self):
        query_all = 'SELECT * FROM task'
        self.cursor.execute(query_all)
        check = self.cursor.fetchall()
        # check if there is any to do tasks
        if not self.cursor.fetchall():
            print("\nYour Todo List is Empty. Create One if You Like\n")

        else:
            task_list = []
            for row in self.cursor:
                one_task_list = [row[0], row[1], row[2], row[3], row[4]]
                task_list.append(one_task_list)

            print(tabulate(task_list, headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                           numalign="center"))
            print('\n')

    def list_doing(self):
        query_doing = "SELECT * FROM task WHERE status = 'doing'"
        self.cursor.execute(query_doing)
        records = self.cursor.fetchall()

        if not records:
            print("\nYou Have Not Started Doing Any Task Yet.\n")
        else:
            done_list = []
            print('\nThese Are The Tasks You Are Currently Doing and Duration Taken\n')
            for row in records:
                start = datetime.strptime(self.start, '%Y-%m-%d %H:%M')
                stop = datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
                start_time, stop_time = start.strftime('%H:%M').split(':'), stop.strftime('%H:%M').split(':')
                hours = int(stop_time[0]) - int(start_time[0])
                minutes = int(stop_time[1]) - int(start_time[1])
                tasks_duration = [row[0], row[1], row[2], hours, minutes]
                done_list.append(tasks_duration)

            print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
                           numalign="center"))
            print('\n')

    def list_done(self):
        query_done = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
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

    def list_section(self, section):
        self.section = section
        #query_section = None

        if self.section == 'done':
            query_section = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'done'"

        elif self.section == 'doing':
            start = datetime.strptime(self.start, '%Y-%m-%d %H:%M')
            query_section = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'doing'"

        self.cursor.execute(query_section)
        records = self.cursor.fetchall()
        if self.cursor.rowcount is None:
            print("You have not finished any task yet.\n")
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

    def move_task(self, task_id, section):
        self.task_id = task_id
        self.section = section

        # check first if the task exits
        check = "SELECT * FROM task WHERE id = ?"
        self.cursor.execute(check, (self.task_id,))
        data = self.cursor.fetchone()
        task_section = data[2]
        if data is None:
            print('Sorry the task does not exits')
        else:
            # check task section if to do or doing
            # print(task_section) <debug here...>
            if task_section == 'todo' and self.section == 'done':
                print('\nSorry! You have not Started doing that Task\n')

            elif task_section == 'done' and (self.section == 'done' or self.section == 'doing'):
                print('\nHey! You have Finished doing that Task\n')

            elif task_section == 'doing' and self.section == 'doing':
                print('\nHey! You are currently doing that Task\n')

            elif (task_section == 'todo' and self.section == 'doing') \
                    or (task_section == 'doing' and self.section == 'done'):

                # get the moved task and display to the user

                if task_section == 'todo':
                    # move the task to the appropriate section
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

                elif task_section == 'doing':

                    # move the task to the appropriate section
                    move_task = "UPDATE task SET status = ?, end_on = ? WHERE id = ?"
                    done_cursor = self.cursor.execute(move_task, (self.section, self.start, self.task_id))
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


