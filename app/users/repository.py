import pymysql
from app.db import get_db

class UserRepository:
    def __init__(self):
        self.conn = get_db()

    def list_all(self):
        with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM T_USERS"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    def create(self, user_name, level):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO T_USERS (USER_NAME, LEVEL) VALUES (%s, %s)"
            cursor.execute(sql, (user_name, level))
            self.conn.commit()
