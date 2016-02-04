from os.path import isfile
import copy

ALIVE = 'o'
DEAD = '.'
STATE_TO_DIGIT = {ALIVE: '1', DEAD: '0'}
DIGIT_TO_STATE = {'1': ALIVE, '0': DEAD}

def get_nums_from_state(state):
    nums = []
    for line in field:
        nums.append([STATE_TO_DIGIT[cell] for cell in line])
    return nums

def get_state_from_num(num):
    state = [DIGIT_TO_STATE[byte] for byte in str(num)]
    return ''.join(state)

def get_from_rules(rules):
    return rules

def save_to_file(filename, filed, rules):
    destFile = open(filename, "w")
    result = "%s %s %s" % (
        str(len(field)),
        str(get_nums_from_state(field)),
        str(get_from_rules(rules)),
    )
    print(result, file = destFile)
    destFile.close()

def load_from_file(filename):
    sourceFile = open(filename, "r")
    data = sourceFile.readlines()
    sourceFile.close()

    square_side, decimal_field, decimal_rules = data[0], data[1], data[2]
    field, rules = create_field_and_rules(square_side, decimal_field, decimal_rules)
    return field, rules

def request_rules():
    entered_values = input('Enter your rules.\n').split()
    start_living = [int(char) for char in entered_values[0]]
    stay_alive = [int(char) for char in entered_values[1]]
    rules = {'start_living': start_living, 'stay_alive': stay_alive}
    return rules

def request_field_params():
    good_input = False
    square_side = int(input("Enter a length of square's side\n"))
    decimal_field = []
    i = 0
    while len(decimal_field) < square_side:
        this_line_number = int(input("Enter decimal number for line number " + str(i + 1) + ' '))
        if len(bin(this_line_number)) - 2 > square_side:
            print('Please, enter another number, which is smaller than', this_line_number, 'for this line.')
        else:
            decimal_field.append(this_line_number)
            i += 1

    return square_side, decimal_field

def create_field_and_rules(square_side = None, decimal_field = None, rules = None):
    if not square_side:
        square_side, decimal_field = request_field_params()
        rules = request_rules()

    binary_field = []
    for line in decimal_field:
        binary_field.append(bin(line)[2:])

    field = []
    for line in binary_field:
        field.append(DEAD * (square_side - len(line)) + get_state_from_num(line))

    return field, rules

def how_many_alive_neighbours(field, index_i, index_j):
    alive_neighbours = 0
    for i in range(index_i - 1, index_i + 2):
        for j in range(index_j - 1, index_j + 2):
            if i == index_i and j == index_j:
                pass
            elif field[i][j] == ALIVE:
                alive_neighbours += 1
    return alive_neighbours

def step(field, rules):
    field_with_kostyl = [['.'] * (len(field) + 2)]
    for line in field:
        field_with_kostyl.append(['.'] + list(line) + ['.'])
    field_with_kostyl.append(['.'] * (len(field) + 2))

    new_field = copy.deepcopy(field_with_kostyl)

    for i in range(1, len(new_field) - 1):
        for j in range(1, len(new_field[i]) - 1):
            alive_neighbours = how_many_alive_neighbours(field_with_kostyl, i, j)
            if field[i - 1][j - 1] == ALIVE:
                if alive_neighbours in rules['stay_alive']:
                    new_field[i][j] = ALIVE
                else:
                    new_field[i][j] = DEAD

            else:
                if alive_neighbours in rules['start_living']:
                    new_field[i][j] = ALIVE
                else:
                    new_field[i][j] = DEAD

    field = []
    for i in range(1, len(new_field) - 1):
        field.append(new_field[i][1:-1])

    return field

def check_before_restart():
    print('Do you really want to restart?\nEnter "yes" or "no"')
    doesUserWant = input()
    while True:
        if doesUserWant == 'yes':
            return True
        elif doesUserWant == 'no':
            return False
        else:
            print('Incorrect answer. Please enter your answer again\n')

def print_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end = '')
        print()

field, rules = create_field_and_rules()
while True:
    print_field(field)
    command = input()
    steps_to_pass = 0
    if command == "":
        steps_to_pass = 1
    elif command.startswith("w "):
        steps_to_pass = int(command.split()[-1])
    elif command.startswith("s "):
        filename = command.split()[1]
        save_to_file(filename, field, rules)
    elif command.startswith("l "):
        filename = command.split()[1]
        if isfile(filename):
            field, rules = load_from_file(filename)
    elif command.startswith("r"):
        if check_before_restart():
            field, rules = create_field_and_rules()
        else:
            steps_to_pass = 0

    for i in range(steps_to_pass):
        field = step(field, rules)