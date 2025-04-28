from controllers.user_controllers import UserController

class UserView:
    @staticmethod
    def login_screen():
        print("=== Đăng nhập ===")
        username = input("Tên đăng nhập: ")
        password = input("Mật khẩu: ")

        if UserController.login(username, password):
            print("Đăng nhập thành công!")
        else:
            print("Đăng nhập thất bại.")

