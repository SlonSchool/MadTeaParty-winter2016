DEAD = '.'
ALIVE = 'o'
state = {'1': ALIVE, '0': DEAD}

def checkIfInputIsIncorrect(decimalNumber, fieldSize):
    return fieldSize < len(bin(decimalNumber)) - 2

def generate_field(length, decimalNum, specialRules):
    binary = bin(decimalNum)[2:]
    field = [DEAD] * (length - len(binary))
    installRules(specialRules)
    for i in binary:
        field.append(state[i])
    return field

def installRules(specialRules):
    s=specialRules
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
    specialRules = bin(int(input('Введите специальные правила для игры \n')))[2:]
    if checkIfInputIsIncorrect(decimalNumber, fieldSize):
        print('Некорректный ввод')
        return userInput()
    else:
        return [fieldSize, decimalNumber, specialRules]

def lifeIteration():
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
inp=userInput()
field = generate_field(*inp)
specialRules=inp[2]
rules=installRules(specialRules)

while True:
    print(''.join(field))
    action = input()
    if 'w' in action:
        letter, numberOfSteps = list(action.split())
        numberOfSteps = int(numberOfSteps)
        for i in range(numberOfSteps):
            lifeIteration()
    elif action == 'r':
        field = generate_field(*userInput())
    else:
        lifeIteration()

