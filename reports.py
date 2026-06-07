from db import conn
import pandas as pd

def generate_report():
    query = "SELECT * FROM trades"
    df =  pd.read_sql(query , conn)
    df.to_excel("trading_report.xlsx" , index = False)
    print("Report Generated Successfully")