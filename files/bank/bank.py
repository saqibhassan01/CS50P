def main():
    x = input("Greetings: ").strip().lower()
    print(value(x))

def value(greeting):
    if "hello" in greeting:
        greeting = ("$0")
    elif "h" in greeting[0]:
        greeting = ("$20")
    else:
        greeting = ("$100")
    return greeting

if __name__ == "__main__":
    main()