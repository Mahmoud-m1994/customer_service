from typing import Dict, Any

import pyodbc


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


def modify_row(table_name, id, data, db_connector, action) -> bool:
    global values
    try:
        cursor = db_connector.cursor()
        if action == "DELETE":
            query = f"DELETE FROM {table_name} WHERE id = ?"
        elif action == "UPDATE":
            query = f"UPDATE {table_name} SET "
            for column, value in data.items():
                query += f"{column} = ?,"
            query = query[:-1] + f" WHERE id = ?"
            values = list(data.values())
            values.append(id)
        else:
            raise ValueError("Invalid action parameter, must be DELETE or UPDATE")
        cursor.execute(query, [id] if action == "DELETE" else values)
        cursor.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error executing query:", e)
        return False
