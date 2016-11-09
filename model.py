import sqlite3
from datetime import datetime
from tabulate import tabulate


class KanBan(object):
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.start = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Create database called tasks

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
        # self.cursor.execute("SELECT MAX(id),title,status,FROM tasks")
        # task = self.cursor.fetchall()
        self.conn.commit()

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
            self.conn.commit()

    def done_task(self, tid):
        self.tid = tid
        check = "SELECT id, status FROM task WHERE id = ?"
        self.cursor.execute(check, (self.tid,))
        data = self.cursor.fetchone()
        if data is None:
            print('Sorry You have not Started doing that Task')
        else:
            done = 'done'
            doing_update = "UPDATE task SET status = ?, end_on = ? WHERE id = ?"
            self.cursor.execute(doing_update, (done, self.start, self.tid))
            self.conn.commit()
            print("You've successfully done the task")

    def list_all(self):
        query_all = 'SELECT * FROM task'
        self.cursor.execute(query_all)
        task_list = []
        for row in self.cursor:
            one_task_list = [row[0], row[1], row[2], row[3], row[4]]
            task_list.append(one_task_list)

        print(tabulate(task_list, headers=["Task Id", "Task Name", "Status", "Start Time", "Finish Time"],
                       numalign="center"))

    def list_doing(self):
        query_todo = "SELECT * FROM task WHERE status = 'doing'"
        self.cursor.execute(query_todo)
        doing_list = []
        for row in self.cursor:
            one_task_list = [row[0], row[1], row[2], row[3], row[4]]
            doing_list.append(one_task_list)

        print(tabulate(doing_list, headers=["Task Id", "Task Name", "Status", "Start Time", "Finish Time"],
                       numalign="center"))

    def list_done(self):
        query_done = "SELECT * FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
        done_list = []
        for row in self.cursor:
            one_task_list = [row[0], row[1], row[2], row[3], row[4]]
            done_list.append(one_task_list)

        print(tabulate(done_list, headers=["Task Id", "Task Name", "Status", "Start Time", "Finish Time"],
                       numalign="center"))

    def duration(self):
        query_done = "SELECT id, title, status, start_on, end_on FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
        records = self.cursor.fetchall()
        all_task = []
        for row in records:
            start = datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
            stop = datetime.strptime(str(row[4]), '%Y-%m-%d %H:%M')
            start_time, stop_time = start.strftime('%H:%M').split(':'), stop.strftime('%H:%M').split(':')
            hours = int(stop_time[0]) - int(start_time[0])
            minutes = int(stop_time[1]) - int(start_time[1])
            tasks_duration = [row[0], row[1], row[2], hours, minutes]
            all_task.append(tasks_duration)
            print(hours, minutes)

        print(tabulate(all_task, headers=["Task Id", "Task Name", "Status", "Hours Taken", "Minutes Taken"],
                       numalign="center"))

