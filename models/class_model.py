from config.db import get_connection

class ClassModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_classes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM LOP")
        return cursor.fetchall()

    def add_class(self, malop, tenlop, MANV):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO LOP (MALOP, TENLOP, MANV) VALUES (?, ?, ?)", (malop, tenlop, MANV))
        self.conn.commit()

    def update_class(self, malop, tenlop, MANV):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE LOP SET TENLOP = ?, MANV = ? WHERE MALOP = ?", (tenlop, MANV, malop))
        self.conn.commit()

    def delete_class(self, malop):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM LOP WHERE MALOP = ?", (malop,))
        self.conn.commit()
