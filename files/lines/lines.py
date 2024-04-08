import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.py') == False:
        sys.exit('Not a Python file')
    reading()
    counting()


def reading():
    count = []
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            count = lines
            return count
    except FileNotFoundError:
        print("File does not exist")

def counting():
    count = reading()
    x = 0
    for line in count:
        if line.lstrip().startswith('#') or line.startswith('\n') or line.isspace():
            pass
        else:
            x += 1
    print(x)

if __name__ == "__main__":
    main()