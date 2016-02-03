##from copy import deepcopy

def print_text():
    f_length = 0
    number = 10 # KOSTYL to enter loop
    while f_length < len(bin(number)) - 2: # first to chars in bin(x) are '0b'
        f_length = int(input('Enter length: '))
        number = int(input('Enter number to fill field: '))
    return f_length, number

def gen_field():
    smth=print_text()
    f_length=smth[0]
    number=smth[1]
    field = [SYMB[0]] * (f_length - (len(bin(number)) - 2))
    for i in bin(number)[2:]:
        field.append(SYMB[int(i)])
    return field

def check_cell(field):
    field = [SYMB[0]] + field + [SYMB[0]]
    new_field=[]
    for i in range(1, len(field) - 1):
        type_cell=0
        if field[i]==SYMB[0] and field[i-1]==SYMB[1]:
            type_cell=1
        elif field[i]==SYMB[1] and SYMB.index(field[i-1])+SYMB.index(field[i+1])==1:
            type_cell=1
        new_field.append(SYMB[type_cell])
    return new_field

def updated(field):
    new_field = check_cell(field) # KOSTYL for border elements
    return new_field

SYMB=['.', 'o']
field = gen_field()
while True:
    print("".join(field))
    flush = input()
    if flush=='w':
        count=int(input('Enter step count: '))
    elif flush=='r':
        field = gen_field()
        continue
    else:
        count=1
    for i in range(count):
        field = updated(field)
