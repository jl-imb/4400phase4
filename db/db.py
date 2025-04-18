import mysql.connector
from flask import render_template

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"DB Error: {str(e)}")
        return 0, 0

def close_connection(conn, cursor):
    cursor.close()
    conn.close()

def return_table():
    conn, cursor = test_connection()
    cursor.execute("Select * from pilot")
    results = cursor.fetchall()
    close_connection(conn, cursor)
    return render_template('home.html', flights = results)

def add_airplane(airplaneID, tailnum, seatcap, speed, locID, type, maintenanced, model, neo):
    if airplaneID == "" or tailnum == "" or seatcap == "" or speed == "" or locID == "" or type == "":
        return 0, "null vals"
    conn, cursor = test_connection()
    cursor.callproc('add_airplane',
                   [(str(airplaneID)), (str(tailnum)),(str(seatcap)), (str(speed)), (str(locID)),
                   (str(type)), (str(maintenanced)), (str(model)), (str(neo))])
    result = next(cursor.stored_results()).fetchone
    status = result['status']
    reason = result['reason']
    return status, reason


