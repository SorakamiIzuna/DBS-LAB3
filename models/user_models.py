from config.db import get_connection

class UserModel:
    @staticmethod
    def login(username, password):
        conn = get_connection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("EXEC SP_SEL_PUBLIC_NHANVIEN ?, ?", username, password)
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            print("Lỗi login:", e)
            return False
        finally:
            conn.close()
 
