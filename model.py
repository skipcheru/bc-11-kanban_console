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
        self.status = 'todo'
        insert_query = 'INSERT INTO task(title, status) VALUES(?, ?)'
        self.cursor.execute(insert_query, (self.title, self.status))
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

    def doing_task(self, tid):
        self.tid = tid
        check = "SELECT * FROM task WHERE id = ?"
        self.cursor.execute(check, (self.tid,))
        data = self.cursor.fetchone()
        if data is None:
            print('Sorry the task does not exits')
        else:
            doing = 'doing'
            doing_update = "UPDATE task SET status = ?, start_on = ? WHERE id = ?"
            self.cursor.execute(doing_update, (doing, self.start, self.tid))
            #
            self.cursor.execute("SELECT * FROM task WHERE id = ?", (self.tid,))
            print("\nGreat! You have started doing\n")
            task = self.cursor.fetchall()
            for row in task:
                task_list = [row[0], row[1], row[2], row[3], row[4]]
            print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                           numalign="center"))
            print('\n')

            self.conn.commit()

    def done_task(self, tid):
        self.tid = tid
        check = "SELECT id, status FROM task WHERE id = ? AND status = 'doing'"
        self.cursor.execute(check, (self.tid,))
        data = self.cursor.fetchone()
        if data is None:
            print('\nSorry! You have not Started doing that Task')
        else:
            done = 'done'
            doing_update = "UPDATE task SET status = ?, end_on = ? WHERE id = ?"
            self.cursor.execute(doing_update, (done, self.start, self.tid))
            #
            self.cursor.execute("SELECT * FROM task WHERE id = ?", (self.tid,))
            print("\nYou've successfully done the task\n")
            task = self.cursor.fetchall()
            for row in task:
                task_list = [row[0], row[1], row[2], row[3], row[4]]
            print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
                           numalign="center"))
            self.conn.commit()
            print('\n')

    def list_all(self):
        query_all = 'SELECT * FROM task'
        self.cursor.execute(query_all)
        # check if there is any to do tasks
        if self.cursor.rowcount is None:
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

        if self.cursor.rowcount is None:
            print("You have not finished any task yet.\n")
        else:
            done_list = []
            print('\nThese Are The Tasks You Are Currently Doing and Duration Taken\n')
            for row in records:
                start = datetime.strptime(self.start, '%Y-%m-%d %H:%M')
                print(start)
                print(self.start)
                stop = datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
                start_time, stop_time = start.strftime('%H:%M').split(':'), stop.strftime('%H:%M').split(':')
                hours = int(stop_time[0]) - int(start_time[0])
                minutes = int(stop_time[1]) - int(start_time[1])
                tasks_duration = [row[0], row[1], row[2], hours, minutes]
                done_list.append(tasks_duration)

            print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
                           numalign="center"))
            print('\n')

    def all_list_done(self):
        query_done = "SELECT * FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
        if self.cursor.rowcount is None:
            print("You have not finished any task yet.\n")
        else:
            done_list = []
            print('\nThese Are The Tasks You Have Completed\n')
            for row in self.cursor:
                one_task_list = [row[0], row[1], row[2], row[3], row[4]]
                done_list.append(one_task_list)

            print(tabulate(done_list, headers=["Task Id", "Task Name", "Status", "Start Time", "Finish Time"],
                           numalign="center"))
            print('\n')

    def list_done(self):
        query_done = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
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

