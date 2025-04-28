from models.user_models import UserModel

class UserController:
    @staticmethod
    def login(username, password):
        return UserModel.login(username, password)
