
from db import conn

def update_trade():
    cursor = conn.cursor()

    trade_id = int(input("Trade Id :"))
    new_exit_price = float(input("New Exit Price"))

    query = """
    update trades
    SET exit_price = %s
    WHERE trade_id = %s
"""
    cursor.execute(query , (new_exit_price , trade_id))
    conn.commit()

    print("Trade Updated Successfully")

    cursor.close()