import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suraj@003",
        database = "trading_journal"
    )

    if conn.is_connected():
        print("✅ MySQL Connected Successfully")

except Exception as e:
    print("❌ Error:", e)

    print("Database Connected")