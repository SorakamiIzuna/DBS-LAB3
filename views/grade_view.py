import tkinter as tk
from tkinter import messagebox

class GradeView:
    def __init__(self, root, masv, manv):
        self.root = root
        self.masv = masv  # Sử dụng masv đã được truyền vào
        self.manv = manv
        self.controller = None
        self.root.title("Nhập bảng điểm sinh viên")

        # Các widget giao diện
        tk.Label(root, text="Mã sinh viên").grid(row=0, column=0)
        tk.Label(root, text="Mã học phần").grid(row=1, column=0)
        tk.Label(root, text="Điểm thi").grid(row=2, column=0)

        self.masv_entry = tk.Entry(root)
        self.mahp_entry = tk.Entry(root)
        self.diemthi_entry = tk.Entry(root)

        self.masv_entry.grid(row=0, column=1)
        self.mahp_entry.grid(row=1, column=1)
        self.diemthi_entry.grid(row=2, column=1)

        # Đặt mã sinh viên vào ô nhập liệu
        self.masv_entry.insert(0, self.masv)  # Gán mã sinh viên vào ô nhập liệu

        tk.Button(root, text="Lưu điểm", command=self.add_grade).grid(row=3, column=0, columnspan=2)

    def set_controller(self, controller):
        self.controller = controller

    def add_grade(self):
        masv = self.masv  # Sử dụng masv đã được truyền vào
        mahp = self.mahp_entry.get()
        diemthi = self.diemthi_entry.get()

        if masv and mahp and diemthi:
            self.controller.add_grade(masv, mahp, diemthi)
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
