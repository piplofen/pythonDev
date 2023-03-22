import sqlite3
import utils as u
import logging as log

u.logStart("log/log.log")


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        if self.connection is None:
            try:
                self.conn = sqlite3.connect("database/database.db")
                self.cur = self.conn.cursor()
                log.info("Successful initialization local database")
                self.createTableUser()
            except sqlite3.Error as e:
                log.error(e)

    def createTableUser(self):
        self.cur.execute("create table if not exists user(id integer primary key, login varchar, password varchar);")
        self.conn.commit()

    def insertData(self, table, key, value):
        pass

    def updateData(self, table, key, value):
        pass


if __name__ == '__main__':
    d = Database()
