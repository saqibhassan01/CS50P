import re

def main():
    html = input("HTML: ")
    parse(html)

def parse(html):
    if match := re.search(r'.+src="(?:https?://)(?:www\.)?youtube\.com/embed/(.+?)"', html):
        return 'https://youtu.be/' + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()


