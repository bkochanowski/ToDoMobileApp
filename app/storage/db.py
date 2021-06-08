import sqlite3
import os


class Database(object):
    def __init__(self):
        path = 'app/storage/'
        # module ntpath has no attribute exist
        if not os.path.exsist(os.path.join(self.path, 'db.sqlite')):
            conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
            cur = conn.cursor()

            sql_tasks = '''CREATE TABLE tasks(id integer primary key, name text not null, details text, 
            date text not null)'''
            sql_shop = '''CREATE TABLE shopping(id integer primary key, name text not null)'''

            cur.execute(sql_tasks)
            cur.execute(sql_shop)

    def db_connect(self):
        conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))

        return conn

    def get_tasks(self, task):
        conn = self.db_connect()
        cur = conn.cursor()

        try:
            sql_tasks = '''SELECT * FROM tasks'''
            cur.execute(sql_tasks)
            conn.commit()
            data = cur.fetchall()

            return data

        except Exception as e:
            print(e)
            return False

    def add_task(self, task: tuple):

        conn = self.db_connect()
        cur = conn.cursor()

        try:
            sql_tasks = 'INSERT INTO tasks(name, details, date) VALUES(?,?,?)'
            cur.execute(sql_tasks, task)
            conn.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def update_task(self, task: list):
        conn = self.db_connect()
        cur = conn.cursor()

        try:
            sql_tasks = '''UPDATE tasks SET name=?, details=?, date=? WHERE name=?'''
            task.append(task[0])
            cur.execute(sql_tasks, task)
            conn.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def delete_task(self, name):
        conn = self.db_connect()
        cur = conn.cursor()

        try:
            sql_tasks = '''DELETE FROM tasks WHERE name=?'''
            cur.execute(sql_tasks, [name])
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False