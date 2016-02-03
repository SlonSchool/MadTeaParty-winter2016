DEAD = '.'
ALIVE = 'o'
state = {'1': ALIVE, '0': DEAD}

def checkIfInputIsIncorrect(decimalNumber, fieldSize):
    return fieldSize < len(bin(decimalNumber)) - 2

def generate_field(length, decimalNum, rulesTemplate):
    binary = bin(decimalNum)[2:]
    field = [DEAD] * (length - len(binary))
    installRules(rulesTemplate)
    for i in binary:
        field.append(state[i])
    return field

def installRules(rulesTemplate):
    s=rulesTemplate
    if len(s)<8:
        s_array=['0']*(8-len(s))
        s_array+=list(s)
        s=''.join(s_array)
    rules={
        '...': state[s[0]],
        '..o': state[s[1]],
        '.o.': state[s[2]],
        '.oo': state[s[3]],
        'o..': state[s[4]],
        'o.o': state[s[5]],
        'oo.': state[s[6]],
        'ooo': state[s[7]]
        }
    return rules

def userInput():
    fieldSize = int(input('Введите размер поля \n'))
    decimalNumber = int(input('Введите десятичное число, соответствующее полю \n'))
    rulesTemplate = bin(int(input('Введите специальные правила для игры \n')))[2:]
    if checkIfInputIsIncorrect(decimalNumber, fieldSize):
        print('Некорректный ввод')
        return userInput()
    else:
        return [fieldSize, decimalNumber, rulesTemplate]

def lifeIteration(field, rules):
    aliveCells=[]
    deadCells=[]
    if rules['.'+str(field[0])+str(field[1])]==ALIVE:
        aliveCells.append(0)
    else:
        deadCells.append(0)

    n=len(field)
    if rules[str(field[n-2])+str(field[n-1])+'.']==ALIVE:
        aliveCells.append(n-1)
    else:
        deadCells.append(n-1)

    for i in range(1, n-1):
            if rules[str(field[i-1]) + str(field[i]) + str(field[i+1])]==ALIVE:
                aliveCells.append(i)
            else:
                deadCells.append(i)

    for i in aliveCells:
        field[i]=ALIVE
    for i in deadCells:
        field[i]=DEAD

def fieldToBinary(field):
    global DEAD
    global ALIVE
    binary = ''
    state = {DEAD: '0', ALIVE: '1'}
    for char in field:
        binary += state[char]
    return binary

def saveField(fieldSize, decimalNumber, rules, fileName):
    saveFile = open(fileName, 'w')
    print(fieldSize, decimalNumber, rules, sep = '\n', file = saveFile)
    saveFile.close()
    return

def loadField(fileName):
    try:
        loadFile = open(fileName, 'r')
        fieldData = loadFile.readlines()
        fieldSize = fieldData[0]
        decimalNumber = fieldData[1]
        rules = fieldData[2]
        loadFile.close()
        return [int(fieldSize), int(decimalNumber, 2), bin(int(rules, 2))[2:]]
    except:
        print('File', fileName, 'does not exist.')

inp=userInput()
field = generate_field(*inp)
rulesTemplate=inp[2]
rules=installRules(rulesTemplate)

while True:
    print(''.join(field))
    action = input()
    if len(action) == 0:
        action = '0'

    if action[0] == 'w':
        letter, numberOfSteps = list(action.split())
        numberOfSteps = int(numberOfSteps)
        for i in range(numberOfSteps):
            lifeIteration()

    elif action == 'r':
        field = generate_field(*userInput())

    elif action[0] == 's':
        fileName = list(action.split())[1]
        saveField(len(field), fieldToBinary(field), rulesTemplate, fileName)

    elif action[0] == 'l':
        fileName = list(action.split())[1]
        fieldData = loadField(fileName)
        '''
        try:
            rules = installRules(fieldData[2])
            field = generate_field(fieldData)
        except:
            pass
        '''
        rules = installRules(fieldData[2])
        field = generate_field(*fieldData)

    else:
        lifeIteration(field, rules)