import pyodbc
from dotenv import load_dotenv
import os

# Load biến môi trường
load_dotenv()

def get_connection():
    try:
        server = os.getenv('DB_SERVER')
        database = os.getenv('DB_DATABASE')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')

        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
            , timeout=5
        )
        print("Kết nối database thành công.")
        return conn
    except pyodbc.Error as e:
        print("Kết nối database thất bại.")
        print("Lỗi:", e)
        return None
