from db import conn
from trade_operations import add_trade
from delete_trade import delete_trade
from view_trades import view_trades
from update_trade import update_trade
from analysis import run_analysis
from reports import generate_report
from charts import show_charts



while True:
  print("\n=====Trading Journal =====")
  print("1. Add Trade")
  print("2. View Trades")
  print("3. Delete Trade")
  print("4. Update Trade")
  print("5. Analysis")
  print("6. Export Report")
  print("7. Charts")
  print("8. Exit")

  choice = input("Enter Your Choice :")

  if choice == "1":
   add_trade()

  elif choice == "2":
    view_trades()

  elif choice == "3":
    trade_id = int(input("Trade Id :"))
    delete_trade(trade_id)

  elif choice == "4":
    update_trade()

  elif choice == "5":
      run_analysis()

  elif choice == "6":
    generate_report()

  elif choice == "7":
    show_charts()

  elif choice == "8":
    print("Exiting...")
    break
  
  else:
    print("Invalid Choice")