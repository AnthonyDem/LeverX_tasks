import pymysql
import sql_queries
from pymysql.cursors import DictCursor
from settings import SETTINGS



class DBops:
    def __init__(self):
        self.connect = pymysql.connect(SETTINGS['host'],
                                       SETTINGS['user'],
                                       SETTINGS['password'],
                                       SETTINGS['db'],
                                       )
        self.cursor = self.connect.cursor()

    def create_table(self):
        for query in sql_queries.CREATE_QUERIES:
            self.cursor.execute(query)

    def insert_queries(self, rooms_file, students_file):
        sql = "INSERT INTO rooms (id, name) VALUES (%s, %s)"
        sql2 = "INSERT INTO students (id ,birthday, name, room_id, sex) VALUES (%s, %s, %s, %s, %s)"
        for room in rooms_file:
            self.cursor.execute(sql, (room['id'],
                                      room['name']))
        for student in students_file:
            self.cursor.execute(sql2, (student['id'],
                                       student['birthday'],
                                       student['name'],
                                       student['room'],
                                       student['sex']))

    def commit(self):
        self.connect.commit()

    def select_query(self, query):
        with self.connect.cursor(DictCursor) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result



