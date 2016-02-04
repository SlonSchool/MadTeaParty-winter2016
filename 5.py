from copy import deepcopy
ALIVE = 'o'
DEAD = '.'
SYMB={'0':DEAD, '1':ALIVE}

def save(field, count_symb, rules, rules2, file_name):
    file1 = open(file_name, "w")
    print(count_symb, '\n',  field, '\n',  rules, rules2, file = file1)
    file1.close()

def load(file_name): ##THERE ARE PROBLEMS
    file1 = open(file_name, "r")
    count_symb = file1.readline()
    pos=[]
    pos=list(file1.readline().split())
    for i in range(count_symb):
        pos[i]=bin(int(pos[i]))[2:]
    field = createField(count_symb, pos)
    return (field, count_symb, rules, rules2)

def fieldToNumber(field):
    bin_number = ''
    for i in field:
        if i == ALIVE:
            bin_number += '1'
        else:
            bin_number += '0'
    number = int(bin_number, 2)
    return number

def createField(count_symb, pos):
    result_str = ['.' for i in range(count_symb)]
    result=[]
    for i in range(count_symb):
        result.append(deepcopy(result_str))
    for i in range(count_symb):
        if count_symb<len(pos[i]):
            return 0
        else:
            zeros=count_symb-len(pos[i])
            for j in range(len(pos[i])):
                if pos[i][j]=='1':
                    result[i][j+zeros]=ALIVE
    return result

def createRulesDict(create, contin):
    result = [dict(), dict()]
    divisor = 128
    while len(create)>=1:
        result[0][create[-1]]=ALIVE
        create=create[:-1]
    while len(contin)>=1:
        result[1][contin[-1]]=ALIVE
        contin=contin[:-1]
    return result

def step(oldField, rules):
    count_symb = len(oldField)
    newField = []
    oldField.append(''.join([DEAD]*(count_symb+2)))
    oldField.insert(0, ''.join([DEAD]*(count_symb+2)))
    for i in range(1, count_symb + 1):
        oldField[i] = DEAD + ''.join(oldField[i]) + DEAD # Borders
        newField.append([])
    for i in range(1, count_symb + 1):
        for j in range(1, count_symb + 1):
            k=0
            for h in range(-1, 2):
                for g in range(-1, 2):
                    if oldField[i+h][j+g]==ALIVE and not (h==0 and g==0):
                        k+=1
            newField[i-1].append(rules[0 if oldField[i][j]==DEAD else 1].get(str(k), DEAD))
    return newField

def printField(field):
    for i in range(len(field)):
        print(''.join(field[i]))

while True:
    field=0
    notrestart=True
    while field == 0:
        count_symb = int(input('Enter size of game: '))
        pos=[]
        for i in range(count_symb):
            pos.append(bin(int(input('Enter field in string '+ str(i+1)+ ': ')))[2:])
        field = createField(count_symb, pos)
        if field==0:
            print('Wrong! Repeat please')
    rulesNumCreate = input('Enter rules of creating life: ')
    rulesNumContinue = input('Enter rules of continuing life: ')
    rules = createRulesDict(rulesNumCreate, rulesNumContinue)
    while notrestart:
        printField(field)
        command = input()
        count=1
        if command == 'w':
            count = int(input('Enter count of iterations: '))
        elif command == 'r':
            notrestart=False
        elif command == 's':
            file_name = input("Enter file's name: ")
            fieldNum=''
            for i in field:
                fieldNum+=str(fieldToNumber(i))
                fieldNum+=' '
            fieldNum=fieldNum[:-1]
            save(fieldNum, count_symb, rulesNumCreate, rulesNumContinue, file_name)
        elif command == 'l':
            file_name = input("Enter file's name: ")
            old = load(file_name)
            field = old[0]
            count_symb = old[1]
            rulesNum = old[2]
            rulesNumContinue = old[3]
            rules = createRulesDict(rulesNumCreate, rulesNumContinue)
            continue
        for i in range(count):
            field = step(field, rules)

