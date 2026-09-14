from flask import Blueprint, request, render_template, redirect, url_for, current_app
from app.db import get_db
from .services import UserService
from .repository import UserRepository

bp = Blueprint("users", __name__)

def get_service():
    return UserService(UserRepository(get_db()))

@bp.route("/")
def index():
    try:
        service = get_service()
        users = service.list_users()
    except Exception as e:
        current_app.logger.exception("查询用户失败: %s", e)
        return render_template("error.html", message="查询失败"), 500
    return render_template("users/index.html", users=users)

@bp.route("/add")
def add():
    return render_template("users/add.html")

@bp.route("/insert", methods=["POST"])
def insert():
    try:
        user_name = request.form.get("user_name")
        level = request.form.get("level")
        service = get_service()
        service.create_user(user_name, level)
    except ValueError as e:
        return render_template("error.html", message=str(e)), 400
    except Exception as e:
        current_app.logger.exception("新增用户失败: %s", e)
        return render_template("error.html", message="新增失败"), 500
    return redirect(url_for("users.index"))
