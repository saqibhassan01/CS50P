import re
import sys


def main():
    lines = input("Text: ")
    count(lines)


def count(s):
    line = len(re.findall(r'\b\W*um\b\W*', s, re.MULTILINE | re.IGNORECASE))
    print(line)


if __name__ == "__main__":
    main()