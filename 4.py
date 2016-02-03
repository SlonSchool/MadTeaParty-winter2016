import copy
import math
import os.path

ALIVE = 'O'
DEAD = '.'

def requestField():
    field = None
    while field == None:
        print("Enter size of field and template")
        size = int(input())
        number = int(input())
        field = createField(size, number)
    return field

def dictiKeysGenerator(zeroValue, oneValue):
    # generates keys like '...', '..O' etc using binary numbers from 0 to 7
    numbers = range(0, 8)
    binNumbers = []
    for elem in numbers:
        binary = bin(elem)[2::]
        while len(binary) < 3:
            binary = '0' + binary
        binNumbers.append(binary)
    keys = []
    symbol = {'1': oneValue, '0': zeroValue}
    for elem in binNumbers:
        keyElem = ''
        for char in elem:
            keyElem += symbol[char]
        keys.append(keyElem)
    return keys

def createRules(decimalNumber):
    global DEAD
    global ALIVE
    binary = bin(decimalNumber)[2:]
    while len(binary) < 8:
        binary = '0' + binary
    state = {'0': DEAD, '1': ALIVE}
    rules = {}
    rulesKeys = dictiKeysGenerator(DEAD, ALIVE)
    for i in range(len(rulesKeys)):
        rules[rulesKeys[i]] = state[binary[i]]
    return rules

def createField(size, number):
    template = str(bin(number))[2:]
    if size < len(template):
        print("Template larger then field size! Try again.")
        return None

    digit_to_state = {'1': ALIVE, '0': DEAD}
    field = [DEAD] * size # изначально все клетки на поле мертвы
    len_difference = size - len(template)
    for i in range(len(template)):
        field[len_difference + i] = digit_to_state[template[i]]

    return field

def fieldToNumber(field):
    code = {DEAD: 0, ALIVE: 1}
    result = 0
    for c in field:
        result *= 2
        result += code[c]
    return result

def rulesToNumber(rulesDict):
    rulesField = ''
    for key in sorted(rulesDict):
        rulesField += rulesDict[key]
    return fieldToNumber(rulesField)

def writeToFile(filename, fieldSize, fieldNum, rulesNum):
    outfile = open(filename, 'w')
    outfile.write(str(fieldSize) + ' ' + str(fieldNum) + ' ' + str(rulesNum) + '\n')
    outfile.close()

def readFromFile(filename): # Returns field string and rules dict
    infile = open(filename)
    fieldSize, fieldNum, rulesNum = map(int, infile.read().split())
    infile.close()
    return createField(fieldSize, fieldNum), createRules(rulesNum)

def checkCell(field, i, rulesDict):
    try:
        return rulesDict[''.join(field)[i - 1:i + 2]] == ALIVE
    except KeyError:
        print(rulesDict)
        print(''.join(field)[i - 1:i + 2])

def updated(field, rules):
    newField = copy.copy(field)
    field = [DEAD] + field + [DEAD]
    # проверка для всех остальных клеток
    for i in range(1, len(field) - 1):
        if checkCell(field, i, rules):
            newField[i - 1] = ALIVE
        else:
            newField[i - 1] = DEAD
    return newField

def main():
    field = requestField()
    rules = createRules(int(input('Enter a decimal number for rules\n')) % 256)

    while True:
        print(''.join(field))
        command = input()
        count = 1
        if command == '':
            count = 1
        elif command == 'w':
            count = int(input('Enter count of steps: '))
        elif command == 'r':
            field = requestField()
            rules = createRules(int(input('Enter a decimal number for rules\n')) % 256)
        elif command[0] == 's':
            filename = command.split()[1]
            writeToFile(filename, len(field), fieldToNumber(field), rulesToNumber(rules))
            count = 0
        elif command[0] == 'l':
            filename = command.split()[1]
            while not os.path.isfile(filename):
                filename = input('Please, provide correct filename: ')
            field, rules = readFromFile(filename)
            count = 0

        for i in range(count):
            field = updated(field, rules)

main()
