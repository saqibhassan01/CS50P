import random
def main():
    level = get_level()
    score  = simulate_game(level)
    print("Score:",score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
            else:
                break
        except(ValueError):
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def simulate_round(x,y):
    tries = 1
    while tries <=3:
        try:
            answer  = (x + y)
            question = (f"{x} + {y} = ")
            quest = int(input(question))
            if quest == (answer):
                return True
            else:
                tries+=1
                print("EEE")
        except:
                tries+=1
                print("EEE")
    print(f"{question}{answer}")
    return False

def simulate_game(level):
    round = 1
    score = 0
    while round <=10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score+=1
        round+=1
    return score

if __name__ == "__main__":
    main()