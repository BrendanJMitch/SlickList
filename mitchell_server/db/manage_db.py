import sqlite3
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DIR_PATH, 'slicklist_db.sqlite')

def create_tables(cursor=None):
    if not os.path.exists(DB_PATH):
        open(DB_PATH, 'a').close()
    with open(os.path.join(DIR_PATH, 'create_tables.sql'), 'r') as sql_file:
        create_tables_cmds = sql_file.read()
    if cursor is None:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
    cursor.executescript(create_tables_cmds)

def drop_tables(cursor=None):
    if cursor is None:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
    tables = get_tables(cursor)
    print(tables)
    for table in tables:
        cmd = f'DROP TABLE IF EXISTS {table}'
        cursor.execute(cmd)   

def get_tables(cursor=None):
    if cursor is None:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
    cmd = "SELECT name FROM sqlite_master WHERE type='table';"
    result = cursor.execute(cmd)
    return [row for row in result.fetchall()]
