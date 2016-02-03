# from copy import deepcopy

DEAD = '.'
ALIVE = 'o'
SYMB = {'0': DEAD, '1': ALIVE}

def print_text():
    good_input = False
    while not good_input:
        f_length = int(input('Enter length: '))
        bin_number = bin(int(input('Enter number to fill field: ')))[2:]
        rules_template = bin(int(input('Enter number to create rules: ')) % 256)[2:]
        good_input = (f_length > len(bin_number))
        if not good_input:
            print("Too long! Try again")
    return f_length, bin_number, rules_template

def gen_field_rules():
    input_info = print_text()
    f_length = input_info[0]
    number = input_info[1]
    rules_template = input_info[2]
    field = [DEAD] * (f_length - len(number))
    for i in number:
        field.append(SYMB[i])

    rules = {}
    rules_template = '0' * (8 - len(rules_template)) + rules_template
    for i in range(8):
        indices = bin(i)[2:]
        indices = '0' * (3 - len(indices)) + indices
        rules[SYMB[indices[0]] + SYMB[indices[1]] + SYMB[indices[2]]] = SYMB[rules_template[i]]

    return field, rules

def check_cell(field, rules, i):
    return rules["".join(field[(i - 1):(i + 2)])]


def updated(field, rules):
    field = [DEAD] + field + [DEAD]
    new_field = []
    for i in range(1, len(field) - 1):
        new_field.append(check_cell(field, rules, i))
    return new_field


field, rules = gen_field_rules()
while True:
    print("".join(field))
    command = raw_input()
    count = 1
    if command == '':
        count = 1
    elif command =='w':
        count = int(raw_input('Enter step count: '))
    elif command =='r':
        field, rules = gen_field_rules()
        continue

    for i in range(count):
        field = updated(field, rules)
