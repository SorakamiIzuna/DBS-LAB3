import tkinter as tk
from views.user_view import LoginScreen

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
