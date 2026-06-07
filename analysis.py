from db import conn

def run_analysis():
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(profit_loss)
    FROM trades
    """)

    result = cursor.fetchone()
    print("Total Profit/Loss =" , result[0])

    cursor.execute("""
    SELECT COUNT(*)
    FROM trades
    WHERE profit_loss > 0
    """
)
    wins = cursor.fetchone()
    print("Winning Trades =" , wins[0])

    cursor.execute("""
    SELECT COUNT(*)
    FROM trades
    WHERE profit_loss < 0
    """)
    losses = cursor.fetchone()
    print("Losing Trades =" , losses[0])

    cursor.close()

