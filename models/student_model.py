from config.db import get_connection

class StudentModel:
    def __init__(self):
        self.conn = get_connection()

    def get_classes_by_user(self, manv):
        cursor = self.conn.cursor()
        cursor.execute("{CALL GetClassesByUser (?)}", (manv,))
        return cursor.fetchall()

    def get_students_by_class(self, malop):
        cursor = self.conn.cursor()
        cursor.execute("{CALL GetStudentsByClass (?)}", (malop,))
        return cursor.fetchall()

    def add_student(self, masv, hoten, ngaysinh, diachi, malop, tendn, matkhau):
        cursor = self.conn.cursor()
        cursor.execute("{CALL AddStudent (?, ?, ?, ?, ?, ?, ?)}",
                       (masv, hoten, ngaysinh, diachi, malop, tendn, matkhau))
        self.conn.commit()

    def update_student(self, masv, hoten, ngaysinh, diachi, tendn):
        cursor = self.conn.cursor()
        cursor.execute("{CALL UpdateStudent (?, ?, ?, ?, ?)}",
                       (masv, hoten, ngaysinh, diachi, tendn))
        self.conn.commit()

    def delete_student(self, masv):
        cursor = self.conn.cursor()
        cursor.execute("{CALL DeleteStudent (?)}", (masv,))
        self.conn.commit()
