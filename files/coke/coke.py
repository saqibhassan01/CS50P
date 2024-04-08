amount = ("Amount Due:",50)
txt , cash = amount
coins = [25, 10, 5 ]
while cash>0:
    print(txt,cash)
    insert = int(input("Insert Coin: "))
    for _ in coins:
        if _ == insert:
            cash = cash - insert
        if cash == 0:
            print(f"Change Owed: {cash}")
            break
        elif cash < 0:
            owed = abs(cash)
            print ("Change Owed:",owed)
            break