import os


def get_connection_string():
    server = os.getenv('SERVER')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    driver = os.getenv('DRIVER')
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return connection_string
