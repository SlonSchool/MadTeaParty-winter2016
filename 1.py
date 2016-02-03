from copy import deepcopy

ALIVE = 'o'
DEAD = '.'

def requestFieldParams():
    print("Enter field length")
    length = int(input())
    print("Enter decimal number")
    decimal = int(input())
    return length, decimal

def createField():
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
    return ''.join(field)

def step(live):
    new = [DEAD] * len(live)
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
            new[i] = DEAD

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