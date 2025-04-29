import tkinter as tk
from tkinter import messagebox

class ClassView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý lớp học")

        self.controller = None

        tk.Label(root, text="Mã lớp").grid(row=0, column=0)
        tk.Label(root, text="Tên lớp").grid(row=1, column=0)
        tk.Label(root, text="Giảng viên").grid(row=2, column=0)

        self.malop = tk.Entry(root)
        self.tenlop = tk.Entry(root)
        self.MANV = tk.Entry(root)

        self.malop.grid(row=0, column=1)
        self.tenlop.grid(row=1, column=1)
        self.MANV.grid(row=2, column=1)

        tk.Button(root, text="Thêm", command=self.add_class).grid(row=3, column=0)
        tk.Button(root, text="Cập nhật", command=self.update_class).grid(row=3, column=1)
        tk.Button(root, text="Xóa", command=self.delete_class).grid(row=3, column=2)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=3)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def set_controller(self, controller):
        self.controller = controller
        self.controller.load_classes()

    def display_classes(self, data):
        self.listbox.delete(0, tk.END)
        for row in data:
            self.listbox.insert(tk.END, f"{row.MALOP} | {row.TENLOP} | {row.MANV}")

    def get_selected_malop(self):
        selection = self.listbox.curselection()
        if selection:
            value = self.listbox.get(selection[0])
            return value.split('|')[0].strip()
        return None

    def on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            values = self.listbox.get(selection[0]).split('|')
            self.malop.delete(0, tk.END)
            self.tenlop.delete(0, tk.END)
            self.MANV.delete(0, tk.END)

            self.malop.insert(0, values[0].strip())
            self.tenlop.insert(0, values[1].strip())
            self.MANV.insert(0, values[2].strip())

    def add_class(self):
        self.controller.add_class(
            self.malop.get(),
            self.tenlop.get(),
            self.MANV.get()
        )

    def update_class(self):
        self.controller.update_class(
            self.malop.get(),
            self.tenlop.get(),
            self.MANV.get()
        )

    def delete_class(self):
        malop = self.get_selected_malop()
        if malop:
            confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?")
            if confirm:
                self.controller.delete_class(malop)
