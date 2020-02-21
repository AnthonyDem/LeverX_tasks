import pymysql
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

    def create_table(self, create_queries):
        for query in create_queries:
            self.cursor.execute(query)

    def insert_data(self, table_name, data_headers, data):
        values = ",".join(["%({})s".format(header) for header in data_headers])
        if table_name == 'rooms':
            self.cursor.executemany("INSERT INTO rooms VALUES {}".format(values), data)
        elif table_name == 'students':
            self.cursor.execute("INSERT INTO students VALUES {}".format(values), data)

    def commit(self):
        self.connect.commit()

    def execute_query(self, query):
        self.connect.cursor(DictCursor).execute(query)
        result = self.cursor.fetchall()
        return result
