DEAD = '.'
ALIVE = 'o'

def checkIfInputIsIncorrect(decimalNumber, fieldSize):
    return fieldSize < len(bin(decimalNumber)) - 2

def generate_field(length, decimalNum):
    binary = bin(decimalNum)[2:]
    field = [DEAD] * (length - len(binary))
    state = {'1': ALIVE, '0': DEAD}
    for i in binary:
        field.append(state[i])
    return field

def userInput():
    fieldSize = int(input('Введите размер поля \n'))
    decimalNumber = int(input('Введите десятичное число, соответствующее полю \n'))

    if checkIfInputIsIncorrect(decimalNumber, fieldSize):
        print('Некорректный ввод')
        return userInput()
    else:
        return [fieldSize, decimalNumber]

def lifeIteration():
    aliveCells=[]
    deadCells=[]
    if field[1]==DEAD:
        deadCells.append(0)

    n=len(field)
    if field[n-2]==DEAD:
        deadCells.append(n-1)
    else:
        aliveCells.append(n-1)

    for i in range(1, n-1):
        if field[i] == ALIVE:
            if (field[i-1]==DEAD and field[i+1]==DEAD) or (field[i-1]==ALIVE and field[i+1]==ALIVE):
                deadCells.append(i)
            else:
                aliveCells.append(i)
        else:
            if field[i-1] == ALIVE:
                aliveCells.append(i)
            else:
                deadCells.append(i)
    for i in aliveCells:
        field[i]=ALIVE
    for i in deadCells:
        field[i]=DEAD

field = generate_field(*userInput())

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
