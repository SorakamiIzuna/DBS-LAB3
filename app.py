from config.db import get_connection

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Connected to Database")
    else:
        print("Unable to connect")
