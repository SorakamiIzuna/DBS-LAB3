from config.db import get_connection

class ClassModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_classes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM LOPHOC")
        return cursor.fetchall()

    def add_class(self, malop, tenlop, giangvien):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO LOPHOC (MALOP, TENLOP, GIANGVIEN) VALUES (?, ?, ?)", (malop, tenlop, giangvien))
        self.conn.commit()

    def update_class(self, malop, tenlop, giangvien):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE LOPHOC SET TENLOP = ?, GIANGVIEN = ? WHERE MALOP = ?", (tenlop, giangvien, malop))
        self.conn.commit()

    def delete_class(self, malop):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM LOPHOC WHERE MALOP = ?", (malop,))
        self.conn.commit()
