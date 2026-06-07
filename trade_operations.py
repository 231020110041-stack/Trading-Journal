from db import conn
from datetime import date

def add_trade():
    cursor = conn.cursor()
    trade_date = date.today()

    symbol = input("Stock Name :")
    trade_type = input("Trade Type (Buy/Sell) :").upper()

    entry = float(input("Entry Price :"))
    exit_price = float(input("Exit Price :"))
    quantity = int(input("Quantity :"))

    if trade_type == "BUY":
        profit_loss = (exit_price - entry) * quantity

    elif trade_type == "SELL" :
        profit_loss = (entry - exit_price) * quantity
        
    else:
        print("Invalid Trade Type")
        return
    
    query = """
   INSERT INTO trades
   (trade_date , symbol ,trade_type, entry_price, exit_price , quantity ,profit_loss)
VALUES(%s,%s,%s,%s,%s,%s,%s)
"""

    values = (trade_date , symbol , trade_type , entry , exit_price , quantity , profit_loss)
    cursor.execute(query , values)
    conn.commit()

    print("Trade Added Successfully")
    cursor.close()