from models.student_model import StudentModel

class StudentController:
    def __init__(self, view, manv):
        self.model = StudentModel()
        self.view = view
        self.manv = manv
        self.view.set_controller(self)

    def load_classes(self):
        classes = self.model.get_classes_by_user(self.manv)
        self.view.display_classes(classes)

    def load_students(self, malop):
        students = self.model.get_students_by_class(malop)
        self.view.display_students(students)

    def add_student(self, masv, hoten, ngaysinh, diachi, tendn, matkhau, malop):
        self.model.add_student(masv, hoten, ngaysinh, diachi, malop, tendn, matkhau)
        self.load_students(malop)

    def update_student(self, masv, hoten, ngaysinh, diachi, tendn, malop):
        self.model.update_student(masv, hoten, ngaysinh, diachi, tendn)
        self.load_students(malop)

    def delete_student(self, masv, malop):
        self.model.delete_student(masv)
        self.load_students(malop)
