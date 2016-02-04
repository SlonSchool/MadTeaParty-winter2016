# from copy import deepcopy

DEAD = '.'
ALIVE = 'o'
SYMB = {'0': DEAD, '1': ALIVE}


def get_input_info():
    f_length = int(input('Enter size of field: '))
    good_input = False
    field_templates = []
    for i in range(f_length):
        while not good_input:
            field_template = (bin(int(input('Enter number to fill row: ')))[2:])
            good_input = (f_length >= len(field_template))
            if not good_input:
                print("Too long! Try again")
            else:
                field_templates.append(field_template)
        good_input = False
    rules_template = input('Enter numbers to create rules: ')
    return f_length, field_templates, rules_template


def gen_rules(rules_template):
    get_alive_rule, stay_alive_rule = rules_template.split()
    rules = {}
    for i in range(8):
        rules[(DEAD, i)] = ALIVE if str(i) in get_alive_rule else DEAD
        rules[(ALIVE, i)] = ALIVE if str(i) in stay_alive_rule else DEAD
    return rules


def gen_1d_field(template):
    result = [DEAD] * (f_length - len(template))
    for i in template:
        result.append(SYMB[i])
    return result


def gen_field_rules():
    input_info = get_input_info()
    f_length = input_info[0]
    field_templates = input_info[1]
    for i in range(len(field_templates)):
        field_templates[i] = field_templates[i].rjust(f_length, '0').replace('0', DEAD).replace('1', ALIVE)
    rules_template = input_info[2]
    rules = gen_rules(rules_template)
    return field_templates, rules, rules_template


def count_alive_neighboors(field, i, j):
    result = 0
    for i1 in range(i - 1, i + 2):
        for j1 in range(j - 1, j + 2):
            if field[i1][j1] == ALIVE:
                result += 1
    result -= int(field[i][j] == ALIVE)
    return result


def check_cell(field, rules, i, j):
    return rules[(field[i][j], count_alive_neighboors(field, i, j))]


def updated(field, rules):
    for i in range(len(field)):
        field[i] = DEAD + field[i] + DEAD
    field = [DEAD * (len(field[0]))] + field + [DEAD * (len(field[0]))]

    new_field = []
    for i in range(1, len(field) - 1):
        new_row = []
        for j in range(1, len(field) - 1):
            new_row.append(check_cell(field, rules, i, j))
        new_field.append(''.join(new_row))
    return new_field


def save_game():
    file_name = input('Enter file name: ')
    with open(file_name, mode='w') as save:
        save.write(str(len(field)))
        save.write(' ')
        save.write(rules_template)
        save.write('\n')
        save.write(''.join(field))


def load_game():
    file_name = input('Enter file name: ')
    with open(file_name, mode='r') as infile:
        f_size, rules_template = infile.readline().replace('\n', '').split(' ', 1)
        field_line = infile.readline()
        field = [field_line[i:i + int(f_size)] for i in range(0, len(field_line), int(f_size))]
    return (field, rules_template)

field, rules, rules_template = gen_field_rules()
while True:
    print("\n".join(field))
    command = input()
    count = 1
    if command == '':
        count = 1
    elif command == 'w':
        count = int(input('Enter steps count: '))
    elif command == 'r':
        field, rules, rules_template = gen_field_rules()
        continue
    elif command == 's':
        save_game()
    elif command == 'l':
        field, rules_template = load_game()
        rules = gen_rules(rules_template)
    if command != 'l':
        for i in range(count):
            field = updated(field, rules)
