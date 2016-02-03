ALIVE = 'o'
DEAD = '.'


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
        print('Введите длину поля и число, описывающее поле')
        count_symb = int(input())
        pos=bin(int(input()))[2:]
        field = createField(count_symb, pos)
        if field==0:
            print('Введите еще раз')
    rulesNum = int(input('Введите число (от 0 до 255), описывающее правила: '))
    rules = createRulesDict(rulesNum)
    while notrestart:

        print(field)
        command = input()
        count=1
        if command == 'w':
            count = int(input('Enter count of iterations: '))
        elif command == 'r':
            notrestart=False
        for i in range(count):
            field = step(field, rules)

