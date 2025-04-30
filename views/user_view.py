import tkinter as tk
from tkinter import messagebox
from controllers.user_controllers import UserController
from views.class_view import ClassView
from controllers.class_controller import ClassController
class LoginView:
    def __init__(self, root, on_success):
        self.root = root
        self.root.title("Đăng nhập hệ thống")
        self.on_success = on_success
        # Cửa sổ
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Tiêu đề
        title_label = tk.Label(root, text="Đăng nhập", font=("Arial", 18))
        title_label.pack(pady=20)

        # Username
        username_label = tk.Label(root, text="Tên đăng nhập:")
        username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Password
        password_label = tk.Label(root, text="Mật khẩu:")
        password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        # Nút đăng nhập
        login_button = tk.Button(root, text="Đăng nhập", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đủ tên đăng nhập và mật khẩu.")
            return

        if UserController.login(username, password):
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.root.destroy()
            self.on_success(username)
        else:
            messagebox.showerror("Thất bại", "Đăng nhập thất bại!")

    