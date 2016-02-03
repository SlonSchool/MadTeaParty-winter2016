from msvcrt import getch
from copy import deepcopy

def gen_field(f_length, g_progression):
    field = ["."] * (f_length + 2) # dem border elements
    i = 0
    while (g_progression ** i < f_length):
        field[g_progression ** i] = "o"
        i += 1
    return field

def updated(field):
    new_field = deepcopy(field)
    for i in range(1, len(field) - 1): # dem border elements[2]
        if field[i + 1] == field[i - 1]:
            new_field[i] = "."
        else:
            new_field[i] = "o"
    return new_field

f_length = int(input())
g_progression = int(input())

field = gen_field(f_length, g_progression)
print("".join(field[1:-1]))
while True:
    flush = input()
    if flush=='w':
        count=10
    else:
        count=1
    for i in range(count):
        field = updated(field)
    print("".join(field[1:-1]))
