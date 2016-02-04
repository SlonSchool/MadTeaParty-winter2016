import copy
import math
import os.path

ALIVE = 'O'
DEAD = '.'
STATE_TO_NUM = {DEAD: 0, ALIVE: 1}


def requestField():
    field = None
    while field is None:
        print("Enter size of field and then templates for each line")
        size = int(input())
        field = createField(size)
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


def createRules(numbersRebirth, numbersStay):
    rules = dict()
    rules[DEAD] = dict()
    rules[ALIVE] = dict()
    for i in range(9):
        if str(i) in numbersRebirth:
            rules[DEAD][i] = ALIVE
        else:
            rules[DEAD][i] = DEAD
        if str(i) in numbersStay:
            rules[ALIVE][i] = ALIVE
        else:
            rules[ALIVE][i] = DEAD
    return rules


def createField(size, nums=None):
    field = []
    for line_num in range(size):
        if nums is None:
            number = int(input())
        else:
            number = nums[line_num]
        template = str(bin(number))[2:]
        if size < len(template):
            print("Template larger then field size! Try again.")
            return None

        digit_to_state = {'1': ALIVE, '0': DEAD}
        new_line = [DEAD] * size
        len_difference = size - len(template)
        for i in range(len(template)):
            new_line[len_difference + i] = digit_to_state[template[i]]
        field.append(new_line)
    return field


def fieldToNumbers(field):
    result = []
    for i in range(len(field)):
        number = 0
        for cell in field[i]:
            number *= 2
            number += STATE_TO_NUM[cell]
        result.append(number)
    return result


def rulesToNumbers(rulesDict):
    rulesRebirth = ''
    rulesStay = ''
    for item in sorted(rulesDict[DEAD].items()):
        if item[1] == ALIVE:
            rulesRebirth += str(item[0])
    for item in sorted(rulesDict[ALIVE].items()):
        if item[1] == ALIVE:
            rulesStay += str(item[0])
    return (rulesRebirth, rulesStay)


def writeToFile(filename, fieldSize, fieldNum, rulesNum):
    outfile = open(filename, 'w')
    outfile.write(str(fieldSize) + '\n')
    for i in range(len(fieldNum)):
        outfile.write(str(fieldNum[i]) + '\n')
    outfile.write(str(rulesNum[0]) + ' ' + str(rulesNum[1]) + '\n')
    outfile.close()


#  Returns field string and rules dict
def readFromFile(filename):
    infile = open(filename)
    fieldSize = int(infile.readline())
    templates = []
    for i in range(fieldSize):
        templates.append(int(infile.readline()))
    numbersRebirth, numbersStay = infile.readline().split()
    infile.close()
    return createField(fieldSize, templates), createRules(numbersRebirth, numbersStay)


def isCellAlive(field, i, j):
    return field[i][j] == ALIVE


def checkCell(field, i, j, rulesDict):
    aliveCount = 0
    aliveCount += isCellAlive(field, i - 1, j - 1)
    aliveCount += isCellAlive(field, i - 1, j)
    aliveCount += isCellAlive(field, i - 1, j + 1)
    aliveCount += isCellAlive(field, i, j - 1)
    aliveCount += isCellAlive(field, i, j + 1)
    aliveCount += isCellAlive(field, i + 1, j - 1)
    aliveCount += isCellAlive(field, i + 1, j)
    aliveCount += isCellAlive(field, i + 1, j + 1)
    return rulesDict[field[i][j]][aliveCount] == ALIVE


def updated(field, rules):
    newField = copy.deepcopy(field)
    field = [[DEAD] * (len(field) + 2)] + field + [[DEAD] * (len(field) + 2)]
    for i in range(1, len(field) - 1):
        field[i] = [DEAD] + field[i] + [DEAD]

    for i in range(1, len(field) - 1):
        for j in range(1, len(field) - 1):
            if checkCell(field, i, j, rules):
                newField[i - 1][j - 1] = ALIVE
            else:
                newField[i - 1][j - 1] = DEAD
    return newField


def main():
    field = requestField()
    rules = createRules(*(input('Enter a decimal number for rules\n').split()))

    while True:
        for i in range(len(field)):
            print(''.join(field[i]))
        command = input()
        count = 1
        if command == '':
            count = 1
        elif command == 'w':
            count = int(input('Enter count of steps: '))
        elif command == 'r':
            field = requestField()
            rules = createRules(*(input('Enter a decimal number for rules\n')).split())
        elif command[0] == 's':
            filename = command.split()[-1]
            writeToFile(filename, len(field), fieldToNumbers(field), rulesToNumbers(rules))
            count = 0
        elif command[0] == 'l':
            filename = command.split()[-1]
            while not os.path.isfile(filename):
                filename = input('Please, provide correct filename: ')
            field, rules = readFromFile(filename)
            count = 0

        for i in range(count):
            field = updated(field, rules)

main()
