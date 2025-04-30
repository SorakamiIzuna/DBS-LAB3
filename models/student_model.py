from config.db import get_connection

class StudentModel:
    def __init__(self):
        self.conn = get_connection()

    def get_classes_by_user(self, manv):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MALOP, TENLOP FROM LOP WHERE MANV = ?", (manv,))
        return cursor.fetchall()

    def get_students_by_class(self, malop):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT MASV, HOTEN, NGAYSINH, DIACHI, TENDN
            FROM SINHVIEN
            WHERE MALOP = ?
        """, (malop,))
        return cursor.fetchall()

    def add_student(self, masv, hoten, ngaysinh, diachi, malop, tendn, matkhau):
        cursor = self.conn.cursor()
        matkhau_varbinary = matkhau.encode('utf-8')
        cursor.execute("""
            INSERT INTO SINHVIEN (MASV, HOTEN, NGAYSINH, DIACHI, MALOP, TENDN, MATKHAU)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (masv, hoten, ngaysinh, diachi, malop, tendn, matkhau_varbinary))
        self.conn.commit()

    def update_student(self, masv, hoten, ngaysinh, diachi, tendn):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE SINHVIEN
            SET HOTEN = ?, NGAYSINH = ?, DIACHI = ?, TENDN = ?
            WHERE MASV = ?
        """, (hoten, ngaysinh, diachi, tendn, masv))
        self.conn.commit()

    def delete_student(self, masv):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM SINHVIEN WHERE MASV = ?", (masv,))
        self.conn.commit()
