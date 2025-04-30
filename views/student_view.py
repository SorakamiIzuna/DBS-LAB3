import tkinter as tk
from tkinter import ttk, messagebox

class StudentView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý sinh viên")
        self.current_class = None

        self.controller = None

        tk.Label(root, text="Chọn lớp:").grid(row=0, column=0)
        self.class_combobox = ttk.Combobox(root, state="readonly")
        self.class_combobox.grid(row=0, column=1)
        self.class_combobox.bind("<<ComboboxSelected>>", self.class_selected)

        self.tree = ttk.Treeview(root, columns=("MASV", "HOTEN", "NGAYSINH", "DIACHI", "TENDN"), show='headings')
        self.tree.heading("MASV", text="Mã SV")
        self.tree.heading("HOTEN", text="Họ tên")
        self.tree.heading("NGAYSINH", text="Ngày sinh")
        self.tree.heading("DIACHI", text="Địa chỉ")
        self.tree.heading("TENDN", text="Tên đăng nhập")
        self.tree.grid(row=1, column=0, columnspan=3)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # Form nhập
        labels = ["Mã SV", "Họ tên", "Ngày sinh (YYYY-MM-DD)", "Địa chỉ", "Tên đăng nhập", "Mật khẩu"]
        self.entries = []
        for i, label in enumerate(labels, start=2):
            tk.Label(root, text=label).grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        self.masv, self.hoten, self.ngaysinh, self.diachi, self.tendn, self.matkhau = self.entries

        # Nút chức năng
        tk.Button(root, text="Thêm", command=self.add_student).grid(row=8, column=0)
        tk.Button(root, text="Cập nhật", command=self.update_student).grid(row=8, column=1)
        tk.Button(root, text="Xóa", command=self.delete_student).grid(row=8, column=2)

    def set_controller(self, controller):
        self.controller = controller
        self.controller.load_classes()

    def display_classes(self, classes):
        self.class_combobox['values'] = [f"{c.MALOP} - {c.TENLOP}" for c in classes]

    def display_students(self, students):
        self.tree.delete(*self.tree.get_children())
        for sv in students:
            self.tree.insert('', 'end', values=(sv.MASV, sv.HOTEN, sv.NGAYSINH, sv.DIACHI, sv.TENDN))

    def class_selected(self, event):
        class_str = self.class_combobox.get()
        self.current_class = class_str.split(' - ')[0]
        self.controller.load_students(self.current_class)

    def on_select(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            for i in range(5):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, values[i])

    def add_student(self):
        if self.current_class:
            self.controller.add_student(
                self.masv.get(),
                self.hoten.get(),
                self.ngaysinh.get(),
                self.diachi.get(),
                self.tendn.get(),
                self.matkhau.get(),
                self.current_class
            )

    def update_student(self):
        if self.current_class:
            self.controller.update_student(
                self.masv.get(),
                self.hoten.get(),
                self.ngaysinh.get(),
                self.diachi.get(),
                self.tendn.get(),
                self.current_class
            )

    def delete_student(self):
        if self.current_class:
            confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?")
            if confirm:
                self.controller.delete_student(self.masv.get(), self.current_class)
