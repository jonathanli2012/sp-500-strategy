from simple_term_menu import TerminalMenu
from buy_hold import *

def main():
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
        elif(selection == 1):
            min = int(input("min: "))
            max = int(input("max: ")) + 1
            range = int(input("range: "))
            buy_hold_day(min,max,range)
        else:
            exit = 1


if __name__ == "__main__":
    main()