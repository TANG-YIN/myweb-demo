import os
import pymysql
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_SERVICE_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_SERVICE_PORT", 3306))
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DB = "HPE_APP"

@app.route("/")
def index():
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB,
            charset='utf8mb4'
        )
        with conn.cursor() as cursor:
            sql = "SELECT * FROM T_USERS"
            cursor.execute(sql)
            rows = cursor.fetchall()
        conn.close()
    except pymysql.Error as e:
        return f"<h3>Error: {e}</h3><br><a href='/'>Return</a>"
    return render_template("users/index.html", users=rows)

@app.route("/add")
def add():
    return render_template("users/add.html")

@app.route("/insert", methods=["POST"])
def insert():
    user_name = request.form.get("user_name")
    level = request.form.get("level")
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB,
            charset='utf8mb4'
        )
        with conn.cursor() as cursor:
            sql = "INSERT INTO T_USERS (USER_NAME, LEVEL) VALUES (%s, %s)"
            cursor.execute(sql, (user_name, level))
            conn.commit()
        conn.close()
        return redirect("/")
    except pymysql.Error as e:
        return f"<h3>Error: {e}</h3><br><a href='/add'>Return</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
