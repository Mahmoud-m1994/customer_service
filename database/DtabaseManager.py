from typing import Dict, Any
from database.DatabaseConnection import create_db_connector
from model.Action import _Action
import json


# DatabaseManager contains functions that Execute:
# 1. general sql_query
# 2. get single/ multiple row(s)
# 3. update and delete a single row


def create_single_row(table_name: str, data: Dict[str, Any]) -> bool:
    db_connector = create_db_connector()
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


def get_single_row(table_name: str, id: int):
    db_connector = create_db_connector()
    try:
        cursor = db_connector.cursor()
        sql_query = f"SELECT * FROM {table_name} WHERE SellerID = ?"
        cursor.execute(sql_query, (id,))
        row = cursor.fetchone()

        if row:
            # Convert row to dictionary
            row_dict = dict(zip([column[0] for column in cursor.description], row))
            cursor.close()
            return json.dumps(row_dict), 200
        else:
            cursor.close()
            return json.dumps({'message': 'Row not found'}), 404
    except Exception as e:
        print("Error executing query:", e)
        return json.dumps({'message': 'Error executing query'}), 500


def get_multiple_rows(sql_query):
    db_connector = create_db_connector()
    try:
        cursor = db_connector.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        cursor.close()
        # Convert rows to a list of dictionaries
        result = [dict(row) for row in rows]
        return result
    except Exception as e:
        print("Error executing query:", e)
        return None


def delete_or_update_row(table_name: str, id: int, action: _Action) -> bool:
    db_connector = create_db_connector()
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
