import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()


def create_db_connector():
    server = os.getenv('SERVER')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    driver = os.getenv('DRIVER')
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful!", conn)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None
