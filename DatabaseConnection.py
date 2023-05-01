import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# getting variable needed to connect to azure SQL DB
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
driver = os.getenv('DRIVER')
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

cnxn = pyodbc.connect(connection_string)
cursor = cnxn.cursor()
cursor.execute('SELECT TOP 3 FirstName FROM [SalesLT].[Customer]')
for row in cursor:
    print(row)

cnxn.close()

