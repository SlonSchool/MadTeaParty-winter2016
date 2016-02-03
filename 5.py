ALIVE = 'o'
DEAD = '.'

def save(field, count_symb, rules, file_name):
    file1 = open(file_name, "w")
    print(field, count_symb, rulesNum, file = file1)
    file1.close()

def load(file_name):
    file1 = open(file_name, "r")
    field, count_symb, rules = map(int, file1.readline().split())
    field = bin(field)[2:]
    field = createField(count_symb, field)
    return (field, count_symb, rules)

def field_to_number(field):
    bin_number = ''
    for i in field:
        if i == ALIVE:
            bin_number += '1'
        else:
            bin_number += '0'
    number = int(bin_number, 2)
    return number

def createField(count_symb, pos):
    result = ['.' for i in range(count_symb)]
    if count_symb<len(pos):
        return 0
    else:
        zeros=count_symb-len(pos)
        for i in range(len(pos)):
            if pos[i]=='1':
                result[i+zeros]=ALIVE
        return ''.join(result)

def nextRulesKey(oldRulesKey):
    i = len(oldRulesKey) - 1
    while i > -1 and oldRulesKey[i] == ALIVE:
        i -= 1
    if i == -1:
        return DEAD * len(oldRulesKey)
    else:
        return oldRulesKey[:i] + ALIVE + DEAD * (len(oldRulesKey) - i - 1)

def createRulesDict(number):
    result = dict()
    key = DEAD * 3
    divisor = 128
    for i in range(2 ** 3):
        result[key] = ALIVE if (number // divisor % 2 == 1) else DEAD
        divisor //=2
        key = nextRulesKey(key)
    return result

def step(oldField, rules):
    count_symb = len(oldField)
    oldField = DEAD + oldField + DEAD # Borders
    newField = []
    for i in range(1, count_symb + 1):
        newField.append(rules[''.join(oldField[i - 1:i + 1 + 1])])
    return ''.join(newField)

while True:
    field=0
    notrestart=True
    while field == 0:
        print('enter size of game, enter your field')
        count_symb = int(input())
        pos=bin(int(input()))[2:]
        field = createField(count_symb, pos)
        if field==0:
            print('Wrong! Repeat please')
    rulesNum = int(input('enter your rules: '))
    rules = createRulesDict(rulesNum)
    while notrestart:

        print(field)
        command = input()
        count=1
        if command == 'w':
            count = int(input('Enter count of iterations: '))
        elif command == 'r':
            notrestart=False
        elif command == 's':
            file_name = input("Enter file's name: ")
            save(field_to_number(field), count_symb, rulesNum, file_name)
        elif command == 'l':
            file_name = input("Enter file's name: ")
            old = load(file_name)
            field = old[0]
            count_symb = old[1]
            rulesNum = old[2]
            rules = createRulesDict(rulesNum)
            continue
        for i in range(count):
            field = step(field, rules)

