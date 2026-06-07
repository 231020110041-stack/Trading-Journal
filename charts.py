from db import conn
import pandas as pd
import matplotlib.pyplot as plt

def show_charts():

    df = pd.read_sql("SELECT * FROM trades" , conn)

    df["Balance"] = df["profit_loss"].cumsum()
    print(df)

    # plot equity curve
    plt.plot(df["Balance"])

    plt.title("Equity Curve") 
    plt.xlabel("Trades")
    plt.ylabel("profit/loss")
    plt.grid()

    plt.show()
    conn.close()