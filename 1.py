from copy import deepcopy

def createField(length, decimalNumber):
    if len(bin(decimalNumber)) - 2 > length:
        print('Entered length is not enough for your number. Please enter new data (length and number) in one string.')
        newLength, newDecimal = list(map(int, input().split()))
        createField(newLength, newDecimal)
    else:
        binary = bin(decimalNumber)[2:]
        field = ['.'] * length
        j = 0
        for i in range(length - len(binary), length):
            field[i] = '.' if binary[j] == '0' else 'o'
            j += 1
        return ''.join(field)

def step(live):
    new = ['.'] * len(live)
    if live[1] == '.':
        new[0] = ('.')
    else:
        new[0] = ('o')

    if live[-2] == '.':
        new[-1] = '.'
    else:
        new[-1] = 'o'

    for i in range(1, len(live) - 1):
        if live[i - 1] == 'o' and live[i + 1] == 'o' or live[i - 1] != 'o' and live[i + 1] != 'o':
            new[i] = ('.')
        else:
            new[i] = ('o')

    live = ''.join(deepcopy(new))
    return live

def checkBeforeRestart():
    print('Do you really want to restart?\nEnter "yes" oder "no"')
    doesUserWant = input()
    if doesUserWant == 'yes':
        return True
    elif doesUserWant == 'no':
        return False
    else:
        print('Incorrect answer. Please enter your answer again\n')
        checkBeforeRestart()

print("Enter field length")
amount = int(input())
print("Enter decimal number")
decimal = int(input())

live = createField(amount, decimal)

while True:
    print(live)
    s = input()
    steps_to_pass = 0
    if s == "":
        steps_to_pass = 1
    if s == "w":
        steps_to_pass = 10
    if s == 'r':
        if checkBeforeRestart():
            newLength = int(input('Enter a new field length\n'))
            newDecimal = int(input('Enter a new decimal number\n'))
            live = createField(newLength, newDecimal)
        else:
            steps_to_pass = 0

    for i in range(steps_to_pass):
        live = step(live)