from copy import deepcopy
from os.path import isfile

ALIVE = 'o'
DEAD = '.'
STATE_TO_DIGIT = {ALIVE: '1', DEAD: '0'}

def get_num_from_state(state): # allows to get a num from a list of ALIVE and DEAD
    line = "".join(state)
    line = line.replace(ALIVE, STATE_TO_DIGIT[ALIVE])
    line = line.replace(DEAD, STATE_TO_DIGIT[DEAD])
    return int(line, 2)

def save_to_file(filename, live, rules):
    destFile = open(filename, "w")

    result = str(len(live))
    result += " " + str(get_num_from_state(live))

    items = sorted(list(rules.items()))
    rule = []
    for item in items:
        rule += item[1]
    result += " " + str(get_num_from_state(rule))

    print(result, file=destFile)
    destFile.close()
    return

def load_from_file(filename):
    source = open(filename, "r")
    length, decimal, rule_template = list(map(int, source.readline().split()))
    field = createField(length, decimal, rule_template)
    return field

def gen_rules(rule, n, k, p):
    global rules
    if n == k:
        if rule[len(rules)] == '0':
            rules[p] = DEAD
        else:
            rules[p] = ALIVE
        return
    else:
        gen_rules(rule, n, k + 1, p + DEAD)
        gen_rules(rule, n, k + 1, p + ALIVE)

def my_rules(rule = -1):
    if rule == -1:
        print('Enter your rules')
        rule = int(input())
    rule = rule % 256
    rule = bin(rule)[2:]
    rule = '0' * (8 - len(rule)) + rule
    return rule

def requestFieldParams():
    print("Enter field length")
    length = int(input())
    print("Enter decimal number")
    decimal = int(input())
    return length, decimal

def createField(length = -1, decimal = -1, rule_template = -1):
    global rules
    good_input = False
    while not good_input and (length == -1):
        length, decimal = requestFieldParams()
        if len(bin(decimal)) - 2 > length:
            print('Entered length is not enough for your number. Retry')
        else:
            good_input = True
    binary = bin(decimal)[2:]
    field = [DEAD] * length
    j = 0
    for i in range(length - len(binary), length):
        field[i] = DEAD if binary[j] == '0' else ALIVE
        j += 1
    rules = dict()
    rule = my_rules(rule_template)
    gen_rules(rule, 3, 0, '')
    return ''.join(field)

def step(live):
    new = []
    live = DEAD + live + DEAD
    for i in range(1, len(live) - 1):
        if rules[live[i - 1] + live[i] + live[i + 1]] == ALIVE:
            new.append(ALIVE)
        else:
            new.append(DEAD)

    live = ''.join(deepcopy(new))
    return live

def checkBeforeRestart():
    print('Do you really want to restart?\nEnter "yes" oder "no"')
    doesUserWant = input()
    while True:
        if doesUserWant == 'yes':
            return True
        elif doesUserWant == 'no':
            return False
        else:
            print('Incorrect answer. Please enter your answer again\n')

rules = dict()
live = createField()
while True:
    print(live)
    s = input()
    steps_to_pass = 0
    if s == "":
        steps_to_pass = 1
    elif s.split()[0] == "w":
        steps_to_pass = int(s.split()[-1])
    elif s.split()[0] == "s":
        filename = s.split()[1]
        save_to_file(filename, live, rules)
    elif s.split()[0] == "l":
        filename = s.split()[1]
        if isfile(filename):
            live = load_from_file(filename)
    elif s == 'r':
        if checkBeforeRestart():
            live = createField()
        else:
            steps_to_pass = 0

    for i in range(steps_to_pass):
        live = step(live)