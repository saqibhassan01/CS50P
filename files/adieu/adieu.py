import inflect

p = inflect.engine()
list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
        namelist = p.join((list))
    except (EOFError):
        break
print(f"Adieu, adieu, to {namelist}")