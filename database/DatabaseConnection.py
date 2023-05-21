import pyodbc
from dotenv import load_dotenv
from utilities.ServerConnector import get_connection_string
load_dotenv()


def create_db_connector():
    connection_string = get_connection_string()
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful!", conn)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None
