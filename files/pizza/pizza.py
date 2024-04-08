import csv
import sys
from tabulate import tabulate
def main():
    valid()
    reading()

def valid():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.csv') == False:
        sys.exit('Not a CSV file')

def reading():
    try:
       with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit('File does not exist')
        
if __name__ == "__main__":
    main()