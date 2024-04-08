def main():
    x = (input("What time is it? "))
    time = convert(x)
    if 7<= time <=8:
        print("breakfast time")
    if 12<= time <=13:
        print("lunch time")
    if 18<= time <=19:
        print("dinner time")

def convert(time):
    hours , minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes



if __name__ == "__main__":
    main()