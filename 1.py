from copy import deepcopy

ALIVE = 'o'
DEAD = '.'

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

def my_rules():
    print('Enter your rules')
    rule = int(input())
    rule = rule % 256
    rule = bin(rule)[2:]
    rule = '0' * (8 - len(rule)) + rule
    #rule = rule[::-1]
    return rule

def requestFieldParams():
    print("Enter field length")
    length = int(input())
    print("Enter decimal number")
    decimal = int(input())
    return length, decimal

def createField():
    global rules
    good_input = False
    while not good_input:
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
    rule = my_rules()
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
    '''new = [DEAD] * len(live)
    if live[1] == DEAD:
        new[0] = DEAD
    elif live[0] == ALIVE:
        new[0] = ALIVE

    if live[-2] == ALIVE:
        new[-1] = ALIVE
    else:
        new[-1] = DEAD

    for i in range(1, len(live) - 1):
        if (live[i - 1] == ALIVE and live[i] == DEAD) or (live[i - 1] != live[i + 1] and live[i] == ALIVE):
            new[i] = ALIVE
        else:
            new[i] = DEAD'''

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
    elif s == 'r':
        if checkBeforeRestart():
            live = createField()
        else:
            steps_to_pass = 0

    for i in range(steps_to_pass):
        live = step(live)