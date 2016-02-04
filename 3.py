from copy import deepcopy

DEAD = '.'
ALIVE = 'o'
state = {'1': ALIVE, '0': DEAD}
state_reverse = {ALIVE: '1', DEAD: '0'}

def check_If_Input_Is_Incorrect(decimalNumber, fieldSize):
    return fieldSize < len(bin(decimalNumber)) - 2

def generate_field(length, numbers):
    stereofield = []
    for decimalNum in numbers:
        monofield = []
        binary = bin(decimalNum)[2:]
        for i in binary:
            monofield.append(state[i])
        monofield = [DEAD] * (length - len(binary)) + monofield
        stereofield.append(monofield)
    return stereofield

def user_Input():
    field = []
    fieldSize = int(input("ENTER FIELD'S SIZE\n"))
    print("ENTER NUMBER'S IN YOUR FIELD")
    for i in range(fieldSize):
        while True:
            number = int(input())
            if number >= 2 ** fieldSize:
                print('uncorrect!')
            else:
                break
        field.append(number)
    print("ENTER YOUR RULES")
    rulesTemplate = list(map(int, input().split()))
    return [fieldSize, field, rulesTemplate]

def life_Iteration(field, rules):
    new = [[DEAD] * (len(field) + 2) for i in range(len(field) + 2)]
    for i in range(len(field)):
        for j in range(len(field[i])):
            new[i + 1][j + 1] = field[i][j]
    for i in range(1, len(new) - 1):
        for j in range(1, len(new[i]) - 1):
            if new[i][j] == DEAD:
                if come_to_a_life(new, rules[0], i, j):
                    field[i - 1][j - 1] = ALIVE
                else:
                    field[i - 1][j - 1] = DEAD
            if new[i][j] == ALIVE:
                if is_alive(new, rules[1], i, j):
                    field[i - 1][j - 1] = ALIVE
                else:
                    field[i - 1][j - 1] = DEAD
    return field
def field_To_Binary(field):
    global DEAD
    global ALIVE
    binary = ''
    state = {DEAD: '0', ALIVE: '1'}
    new_field = []
    for i in range(len(field)):
        binary = ''
        for char in field[i]:
            binary += state[char]
        new_field.append(int(binary, 2))
    return new_field

def save_Field(fieldSize, save_field, rules, fileName):
    saveFile = open(fileName, 'w')
    print(fieldSize, file = saveFile)
    for i in save_field:
        print(i, file = saveFile)
    print(rules[0], file = saveFile)
    print(rules[1], file = saveFile)
    saveFile.close()
    return

def load_Field(fileName):
    try:
        field = []
        loadFile = open(fileName, 'r')
        fieldSize = int(loadFile.readline())
        for i in range(fieldSize):
            number = int(loadFile.readline())
            field.append(number)
        field = generate_field(fieldSize, field)
        rule1 = loadFile.readline()
        rule2 = loadFile.readline()
        rules = [rule1, rule2]
        loadFile.close()
        return [int(fieldSize), field, rules]
    except:
        print('File', fileName, 'does not exist.')

def come_to_a_life(field, rule, x1, y1):
    count = 0
    x = [-1, 0, 0, 1, -1, -1, 1, 1]
    y = [0, 1, -1, 0, -1, 1, -1, 1]
    for i in range(8):
        #print(x1 + x[i], y1 + y[i])
        count += int(state_reverse[field[x1 + x[i]][y1 + y[i]]])
    return str(rule).find(str(count)) != -1

def is_alive(field, rule, x1, y1):
    count = 0
    x = [-1, 0, 0, 1, -1, -1, 1, 1]
    y = [0, 1, -1, 0, -1, 1, -1, 1]
    for i in range(8):
        count += int(state_reverse[field[x1 + x[i]][y1 + y[i]]])
    return str(rule).find(str(count)) != -1

fieldsize, field, rulesTemplate = user_Input()
save_field = deepcopy(field)
field = generate_field(fieldsize, field)
while True:
    for i in field:
        print("".join(i))
    action = input()
    if len(action) == 0:
        action = '0'
    if action[0] == 'w':
        letter, numberOfSteps = list(action.split())
        numberOfSteps = int(numberOfSteps)
        for i in range(numberOfSteps):
            life_Iteration(field, rulesTemplate)

    elif action == 'r':
        fieldsize, field, rulesTemplate = user_Input()
        field = generate_field(fieldsize, field)

    elif action[0] == 's':
        fileName = list(action.split())[1]
        save_Field(len(field), field_To_Binary(field), rulesTemplate, fileName)

    elif action[0] == 'l':
        fileName = list(action.split())[1]
        fieldData = load_Field(fileName)
        '''
        try:
            rules = install_Rules(fieldData[2])
            field = generate_field(fieldData)
        except:
            pass
        '''
        rulesTemplate = fieldData[2]
        fieldSize = fieldData[0]
        field = fieldData[1]
    else:
        life_Iteration(field, rulesTemplate)