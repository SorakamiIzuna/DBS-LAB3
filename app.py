import tkinter as tk
from controllers.user_controllers import UserController
from views.user_view import LoginView
from controllers.class_controller import ClassController
from views.class_view import ClassView
from views.student_view import StudentView
from controllers.student_controller import StudentController
from session import current_user

def on_login_success(manv):
    current_user["MANV"] = manv
    open_class_view(manv)


def open_class_view(manv):
    root = tk.Tk()
    class_view = ClassView(root, manv)
    controller = ClassController(class_view, manv)
    class_view.set_controller(controller)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login_view = LoginView(root, on_login_success)
    root.mainloop()

