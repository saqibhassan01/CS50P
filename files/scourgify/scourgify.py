import sys
import csv

def main():
    valid()
    firstname = read()
    firstnames(firstname)


def valid():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.csv') == False or sys.argv[2].endswith('.csv') == False:
        sys.exit('Not a CSV file')

def read():
    students= []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for rows in reader:
            name,house= rows["name"],rows["house"]
            last,first=name.split(",")
            formatted_name = f"{first.strip()}, {last.strip()}"
            students.append((formatted_name, house))
    return students

def firstnames(firstname):
    with open("after.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for name, house in firstname:
            writer.writerow([name, house])


if __name__ == "__main__":
    main()
