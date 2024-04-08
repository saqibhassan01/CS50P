from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figfonts = figlet.getFonts()

if len(sys.argv) == 1:
    x = input("Input: ")
    figlet = Figlet(font=random.choice(figfonts))
    print (figlet.renderText(x))
elif len(sys.argv) ==3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--f") and sys.argv[2] in figfonts:
        f = sys.argv[2]
        figlet.setFont(font=f)
        y = input("Input: ")
        print (figlet.renderText(y))
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)