camelCase = input('camelCase: ')
snake_case = ''

for letter in camelCase:

    if letter.isupper():

        snake_case = snake_case + '_' + letter
    else:
        snake_case += letter

print(snake_case.lower())