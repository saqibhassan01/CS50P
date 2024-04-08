while True:
    try:
        fuel = (input("Fraction:")).split("/")
        x , y = (fuel)
        x = int(x)
        y = int(y)
        total = (x * 100 / y )
        total = int(total)
        if total >= 100:
            print("F")
            break
        elif total <= 1:
            print("E")
            break
        else:
            print(total,end="%")
            break
    except (ValueError , ZeroDivisionError):
        pass