from models.grade_model import GradeModel  # Import model vào controller
from tkinter import messagebox

class GradeController:
    def __init__(self, view, current_student, manv):
        self.view = view
        self.current_student = current_student
        self.manv = manv
        self.model = GradeModel(current_student, manv)

    def add_grade(self, masv, mahp, diemthi):
        # Lấy Public Key từ cơ sở dữ liệu
        public_key = self.model.get_public_key()
        if not public_key:
            messagebox.showerror("Lỗi", "Không tìm thấy Public Key!")
            return
        
        # Mã hóa điểm thi
        encrypted_grade = self.model.encrypt_grade(diemthi, public_key)

        # Lưu điểm thi vào cơ sở dữ liệu
        self.model.save_grade(masv, mahp, encrypted_grade)

        messagebox.showinfo("Thành công", "Điểm thi đã được lưu!")
