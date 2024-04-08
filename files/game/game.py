from random import randint

try:
    x = int(input("Level: "))
    guess = randint(1,x)
except (ValueError):
    pass

while True:
    try:
        game = int(input("Guess: "))
        if game < guess:
            print("Too Small!")
        elif game > guess:
            print("Too Large!")
        else:
            print("Just right!")
            break

    except (ValueError):
        pass