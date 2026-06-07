from db import conn

def delete_trade(trade_id):
    cursor = conn.cursor()

    query = "DELETE FROM trades WHERE trade_id = %s"

    cursor.execute(query, (trade_id,))
    conn.commit()

    print("Trade Deleted Successfully")

    cursor.close()