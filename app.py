import os
import pymysql
from flask import Flask, request, render_template_string

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_SERVICE_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_SERVICE_PORT", 3306))
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DB = "HPE_APP"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Python Kubernetes Demo</title><head>
<body align="center">
    <br><br><br><br><br><br>
    <h3>Please input your info</h3>
    <form action="/insert" method="post">
        Your Name: <input type="text" name="user_name"><br><br>
        Your Level: <input type="text" name="level" value="100"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

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
        return "<h3>Success add your info</h3><br><a href='/'>Return</a>"
    except pymysql.Error as e:
        return f"<h3>Error: {e}</h3><br><a href='/'>Return</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
