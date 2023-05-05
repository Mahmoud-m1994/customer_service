from typing import Dict, Any

import pyodbc

from model.Action import _Action


# DatabaseManager contains functions that Execute:
# 1. general sql_query
# 2. get single/ multiple row(s)
# 3. update and delete a single row


def create_single_row(table_name: str, data: Dict[str, Any], db_connector: pyodbc.Connection) -> bool:
    try:
        cursor = db_connector.cursor()
        columns = ', '.join(data.keys())
        values = ', '.join('?' * len(data))
        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})", list(data.values()))
        cursor.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error executing query:", e)
        return False


def get_single_row(table_name: str, id: int, db_connector: pyodbc.Connection):
    try:
        cursor = db_connector.cursor()
        sql_query = f"SELECT * FROM {table_name} WHERE id = {id}"
        cursor.execute(sql_query)
        row = cursor.fetchone()
        cursor.close()
        return row
    except Exception as e:
        print("Error executing query:", e)
        return None


def get_multiple_rows(sql_query, db_connector):
    try:
        cursor = db_connector.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
        print("Error executing query:", e)
        return None


def delete_or_update_row(table_name: str, id: int, db_connector, action: _Action) -> bool:
    try:
        cursor = db_connector.cursor()
        if action == _Action.DELETE:
            query = f"DELETE FROM {table_name} WHERE id = ?"
        elif action == _Action.UPDATE:
            query = f"UPDATE {table_name} SET "
            query += f" WHERE id = ?"
        else:
            raise ValueError("Invalid action parameter, must be DELETE or UPDATE")
        cursor.execute(query, [id])
        cursor.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error executing query:", e)
        return False
