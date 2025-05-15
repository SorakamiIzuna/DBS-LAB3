from config.db import get_connection

class ClassModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_classes(self):
        cursor = self.conn.cursor()
        cursor.execute("{CALL GetAllClasses}")
        return cursor.fetchall()

    def add_class(self, malop, tenlop, MANV):
        cursor = self.conn.cursor()
        cursor.execute("{CALL AddClass (?, ?, ?)}", (malop, tenlop, MANV))
        self.conn.commit()

    def update_class(self, malop, tenlop, MANV):
        cursor = self.conn.cursor()
        cursor.execute("{CALL UpdateClass (?, ?, ?)}", (malop, tenlop, MANV))
        self.conn.commit()

    def delete_class(self, malop):
        cursor = self.conn.cursor()
        cursor.execute("{CALL DeleteClass (?)}", (malop,))
        self.conn.commit()
