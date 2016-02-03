from msvcrt import getch
from copy import deepcopy

def gen_field(f_length):
    field = ["."] * f_length
    i = 0
    while (2 ** i < f_length):
        field[2 ** i] = "o"
        i += 1
    return field

def updated(field):
    new_field = ['.'] + deepcopy(field) + ['.']
    for i in range(1, len(field) - 1): # dem border elements[2]
        if field[i + 1] == field[i - 1]:
            new_field[i] = "."
        else:
            new_field[i] = "o"
    return new_field[1:-1]

field = gen_field(200)
while True:
    flush = input()
    field = updated(field)
    print("".join(field))
