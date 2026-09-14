from .repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def list_users(self):
        return self.repo.list_all()

    def create_user(self, user_name, level):
        if not user_name or not user_name.strip():
            raise ValueError("用户名不能为空")
        if not level or not level.strip():
            raise ValueError("等级不能为空")
        return self.repo.create(user_name.strip(), level)
