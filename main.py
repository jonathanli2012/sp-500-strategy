from simple_term_menu import TerminalMenu
from buy_hold import *
import yfinance as yf
import pandas

def main():
    tick_str = input("Ticker: ")
    tick = yf.Ticker(tick_str)
    tick_history = tick.history(period="max")
    #data = parse(tick.history(period="max"))
    #tick_history.to_csv('tmp.csv', encoding='utf-8', index=True)
    print(tick_history)

    exit = 0
    while(exit == 0):
        title = "Select Mode"
        main_menu = TerminalMenu(["Buy and Hold: Yr", "Buy and Hold: Day", "Exit"],title)
        selection = main_menu.show()
        if(selection == 0):
            min = int(input("min: "))
            max = int(input("max: ")) + 1
            range = int(input("range: "))
            buy_hold_year(min,max,range)
            #buy_hold_year(data, min, max,range)
        elif(selection == 1):
            min = int(input("min: "))
            max = int(input("max: ")) + 1
            range = int(input("range: "))
            buy_hold_day(min,max,range)
            #buy_hod_day(data, min, max, range)
        else:
            exit = 1


if __name__ == "__main__":
    main()