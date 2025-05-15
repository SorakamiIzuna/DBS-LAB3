from models.user_models import UserModel
from session import current_prkey
class UserController:
    @staticmethod
    def login(username, password):
        current_prkey["PASS"]=password
        return UserModel.login(username, password)
