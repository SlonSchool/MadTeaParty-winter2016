from copy import deepcopy

def gen_field():
    f_length = 0
    number = 10 # KOSTYL to enter loop
    while f_length < len(bin(number)) - 2: # first to chars in bin(x) are '0b'
        f_length = int(input('Enter length: '))
        number = int(input('Enter number to fill field: '))
    field = ["."] * (f_length - (len(bin(number)) - 2))
    field += list(bin(number)[2:].replace('0', '.').replace('1', 'o'))
    return field

def updated(field):
    field = ['.'] + field + ['.']
    new_field = deepcopy(field) # KOSTYL for border elements
    for i in range(1, len(field) - 1):
        if field[i + 1] == field[i - 1]:
            new_field[i] = "."
        else:
            new_field[i] = "o"
    return new_field[1:-1]

field = gen_field()
while True:
    print("".join(field))
    flush = input()
    if flush=='w':
        count=10
    elif flush=='r':
        field = gen_field()
        continue
    else:
        count=1
    for i in range(count):
        field = updated(field)
