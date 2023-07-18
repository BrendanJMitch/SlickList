import sqlite3
import os
from src.db.manage_db import get_connection

class Accessor:

    table = ''
    model_class = None

    def __init__(self):
        self.connection = get_connection()

    def get(self, id):
        cmd = f'SELECT FROM {self.table} WHERE id = ?'
        cursor = self.connection.cursor()
        result = cursor.execute(cmd, id)
        model = self.model_class(result.fetchone())
        return model

    def get_many(self, ids):
        cmd = f'SELECT FROM {self.table} WHERE id = ?'
        cursor = self.connection.cursor()
        result = cursor.executemany(cmd, ids)
        models = [self.model_class(row) for row in result.fetchall()]
        return models

    def insert(self, model):
        values = model.__tuple__()
        qmarks = self._get_qmarks(len(values))
        cmd = f'INSERT INTO {self.table} VALUES({qmarks})'
        cursor = self.connection.cursor()
        result = cursor.execute(cmd, values)
        self.connection.commit()

    def insert_many(self, models):
        values = [model.__tuple__() for model in models]
        qmarks = self._get_qmarks(len(values[0]))
        cmd = f'INSERT INTO {self.table} VALUES({qmarks})'
        cursor = self.connection.cursor()
        result = cursor.executemany(cmd, values)
        self.connection.commit()


    def update(self, id, model):
        pass

    def _get_qmarks(self, n):
        qmark_list = ['?' for _ in range(n)]
        return ', '.join(qmark_list)

    def __del__(self):
        self.connection.close()   
