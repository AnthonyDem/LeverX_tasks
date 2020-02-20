import pymysql
from pymysql.cursors import DictCursor


def create_table( creation_sql_table, settings):
    connect = pymysql.connect(**settings)
    try:
        connect.cursor().execute(creation_sql_table)
        connect.commit()
    finally:
        connect.close()

def dump_data():