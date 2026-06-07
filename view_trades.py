from db import conn

def view_trades():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trades")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()