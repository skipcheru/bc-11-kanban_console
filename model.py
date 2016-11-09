import sqlite3
from datetime import datetime

class KanBan(object):
    
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.start = datetime.now().replace(microsecond=0)
        
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
        #self.cursor.execute("SELECT MAX(id),title,status,FROM tasks")
        #task = self.cursor.fetchall()
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
        check = "SELECT id FROM task WHERE id = ?"
        self.cursor.execute(check, (self.tid,))
        data = self.cursor.fetchone()
        if data is None:
            print('Sorry the task does not exits')
        else:
            done = 'done'
            doing_update = "UPDATE task SET status = ?, end_on = ? WHERE id = ?"
            self.cursor.execute(doing_update, (done, self.start, self.tid))
            self.conn.commit()
            #print("You've successfully done the task")

    def list_all(self):
        query_all = 'SELECT * FROM task'
        self.cursor.execute(query_all)

        for row in self.cursor:
            print('{0} : {1}, {2} {3}'.format(row[0], row[1], row[2], row[3]))

    def list_doing(self):
        query_todo = "SELECT * FROM task WHERE status = 'doing'"
        self.cursor.execute(query_todo)
        for row in self.cursor:
            print('{0} : {1}, {2} {3} '.format(row[0], row[1], row[2], row[3]))

    def list_done(self):
        query_done = "SELECT * FROM task WHERE status = 'done'"
        self.cursor.execute(query_done)
        for row in self.cursor:
            print('{0} : {1}, {2} {3}'.format(row[0], row[1], row[2], row[3]))





kanban = KanBan()
kanban.done_task(10)
#kanban.list_all()