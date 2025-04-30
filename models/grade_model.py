import os
import base64
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from config.db import get_connection

class GradeModel:
    def __init__(self, current_student, manv):
        self.current_student = current_student
        self.manv = manv
        self.connection = get_connection()

    def get_public_key(self):
        """
        Đọc file XML public key theo tên MANV và chuyển đổi thành đối tượng RSA key.
        File nằm ở: D:/Temp/public_<MANV>.xml
        """
        file_path = f"D:/Temp/public_{self.manv}.xml"  # Ví dụ: D:/Temp/public_NV01.xml
        if not os.path.exists(file_path):
            print(f"[ERROR] Không tìm thấy file: {file_path}")
            return None

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            modulus_b64 = root.find("Modulus").text
            exponent_b64 = root.find("Exponent").text

            modulus = int.from_bytes(base64.b64decode(modulus_b64), byteorder='big')
            exponent = int.from_bytes(base64.b64decode(exponent_b64), byteorder='big')

            rsa_key = RSA.construct((modulus, exponent))
            return rsa_key
        except Exception as e:
            print(f"[ERROR] Lỗi khi đọc public key XML: {e}")
            return None

    def encrypt_grade(self, grade, public_key):
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_grade = cipher.encrypt(str(grade).encode())
        return encrypted_grade  # Trả về bytes trực tiếp


    def save_grade(self, masv, mahp, encrypted_grade):
        """
        Lưu điểm đã mã hóa vào CSDL
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO BANGDIEM (MASV, MAHP, DIEMTHI)
            VALUES (?, ?, ?)
        """, (masv, mahp, encrypted_grade))
        self.connection.commit()
