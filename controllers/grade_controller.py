from models.grade_model import GradeModel  # Import model vào controller
from tkinter import messagebox

class GradeController:
    def __init__(self, view, current_student, manv):
        self.view = view
        self.current_student = current_student
        self.manv = manv
        self.model = GradeModel(current_student, manv)

    def add_grade(self, masv, mahp, diemthi):
        self.model.save_grade(masv, mahp, diemthi)
        
        messagebox.showinfo("Thành công", "Điểm thi đã được lưu!")
