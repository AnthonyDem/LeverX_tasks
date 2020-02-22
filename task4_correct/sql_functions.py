import pymysql
from pymysql.cursors import DictCursor
from settings import SETTINGS
from sql_queries import Queries


class DBops:
    def __init__(self):
        self.connect = pymysql.connect(SETTINGS['host'],
                                       SETTINGS['user'],
                                       SETTINGS['password'],
                                       SETTINGS['db'],
                                       )
        self.cursor = self.connect.cursor()

    def create_table(self):
        for query in Queries.create_queries():
            self.cursor.execute(query)

    def insert_queries(self, rooms_file, students_file):
        rooms = make_tuple(rooms_file)
        students = make_tuple(students_file)
        sql = "INSERT INTO rooms (id, name) VALUES (%s, %s)"
        sql2 = "INSERT INTO students (id, name, birthday, room_id, sex) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.executemany(sql, rooms)
        self.cursor.executemany(sql2, students)

    def commit(self):
        self.connect.commit()

    def select_query(self, query):
        self.connect.cursor(DictCursor).execute(query)
        result = self.cursor.fetchall()
        return result


def make_tuple(data):
    return [tuple(item.values()) for item in data]
