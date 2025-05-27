# repository/mysql_repository.py

import pymysql
import os

class MysqlRepository:
    def __init__(self, table_name):
        self.table_name = table_name
        self.conn_params = {
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT", "3306")),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "cursorclass": pymysql.cursors.DictCursor
        }

    def execute(self, query, params=None):
        with pymysql.connect(**self.conn_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return cursor.fetchall()

    def get_all(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.execute(query)

    def get_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        return self.execute(query, (id,))

    def insert(self, data: dict):
        keys = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})"
        self.execute(query, tuple(data.values()))
        return {"status": "inserted"}

    def update(self, id, data: dict):
        set_clause = ", ".join([f"{k} = %s" for k in data.keys()])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s"
        self.execute(query, tuple(data.values()) + (id,))
        return {"status": "updated", "id": id}

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = %s"
        self.execute(query, (id,))
        return {"status": "deleted", "id": id}
