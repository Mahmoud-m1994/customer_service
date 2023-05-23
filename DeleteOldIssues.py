import pyodbc
import datetime
from utilities.ServerConnector import get_connection_string


def delete_old_issues():
    try:
        connection_string = get_connection_string()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        current_datetime = datetime.datetime.now()

        cutoff_datetime = current_datetime - datetime.timedelta(days=30)

        cutoff_datetime_str = cutoff_datetime.strftime('%Y-%m-%d %H:%M:%S')

        sql_query = f"DELETE FROM Issues WHERE IssueDate < ?"
        cursor.execute(sql_query, cutoff_datetime_str)
        connection.commit()

        cursor.close()
        connection.close()

        print("Old issues deleted successfully.")
    except Exception as e:
        print("Error deleting old issues:", e)


if __name__ == '__main__':
    delete_old_issues()
