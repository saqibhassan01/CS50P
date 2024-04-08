import re

def main():
    ipaddress = input("IPv4 Address: ")
    validate(ipaddress)

def validate(ipaddress):
    try:
        if ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ipaddress):
            segments = [int(ip.group(i)) for i in range(1, 5)]
            if all(0 <= segment <= 255 for segment in segments):
                print("True")
            else:
                print("False")
        else:
            print("False")
    except ValueError:
        print("False")

if __name__ == "__main__":
    main()
