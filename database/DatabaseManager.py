from typing import Dict, Any
from database.DatabaseConnection import create_db_connector
from model.Action import _Action
import json


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


def get_multiple_rows(table_name: str, order_by: str):
    db_connector = create_db_connector()
    try:
        cursor = db_connector.cursor()
        sql_query = f"SELECT * FROM {table_name} ORDER BY {order_by} DESC"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        cursor.close()
        result = []
        for row in rows:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[columns[i]] = value
            result.append(row_dict)
        return result
    except Exception as e:
        print("Error executing query:", e)
        return None


def delete_or_update_row(table_name: str, id: int, id_str: str, action: _Action, data: Dict[str, Any] = None) -> bool:
    db_connector = create_db_connector()
    try:
        cursor = db_connector.cursor()
        if action == _Action.DELETE:
            query = f"DELETE FROM {table_name} WHERE {id_str} = ?"
            cursor.execute(query, [id])
        elif action == _Action.UPDATE:
            if data is None:
                raise ValueError("Data parameter is required for UPDATE action")
            columns = ', '.join(f"{column} = ?" for column in data.keys())
            values = list(data.values())
            query = f"UPDATE {table_name} SET {columns} WHERE {id_str} = ?"
            values.append(id)
            cursor.execute(query, values)
        else:
            raise ValueError("Invalid action parameter, must be DELETE or UPDATE")

        cursor.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error executing query:", e)
        return False


def add_product_to_order(order_id: int, product_id: int, quantity: int) -> bool:
    db_connector = create_db_connector()
    try:
        cursor = db_connector.cursor()
        cursor.execute("INSERT INTO OrderProducts (OrderID, ProductID, Quantity) VALUES (?, ?, ?)",
                       (order_id, product_id, quantity))
        cursor.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error executing query:", e)
        return False