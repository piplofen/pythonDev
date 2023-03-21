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
                log.info("Initialization local database")
            except sqlite3.Error as e:
                log.error(e)


if __name__ == '__main__':
    d = Database()
