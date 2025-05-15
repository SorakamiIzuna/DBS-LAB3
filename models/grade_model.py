import os
import base64
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from config.db import get_connection
from session import current_user, current_prkey
class GradeModel:
    def __init__(self, current_student, manv):
        self.current_student = current_student
        self.manv = manv
        self.connection = get_connection()
    def save_grade(self, masv, mahp, diemthi):
        """
        Lưu điểm đã mã hóa vào CSDL
        """
        cursor = self.connection.cursor()
        cursor.execute(
        "{CALL SAVE_GRADE (?, ?, ?, ?, ?)}",
        (masv, mahp, diemthi, current_prkey["PASS"], current_user["MANV"]))
        self.connection.commit()

