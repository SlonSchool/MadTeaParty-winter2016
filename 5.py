def createField(count_symb, pos):
    result = ['.' for i in range(count_symb)]
    if count_symb<len(pos):
        return 0
    else:
        zeros=count_symb-len(pos)
        for i in range(len(pos)):
            if pos[i]=='1':
                result[i+zeros]='o'
        return ''.join(result)

def step(oldField, count_symb):
    oldField = '.' + oldField + '.' # Borders
    newField = []
    for i in range(1, count_symb + 1):
        if oldField[i] == '.':
            if oldField[i - 1] == 'o':
                newField.append('o')
            else:
                newField.append('.')
        else:
            if oldField[i - 1] != oldField[i + 1]:
                newField.append('o')
            else:
                newField.append('.')
    return ''.join(newField)

while True:
    field=0
    notrestart=True
    while field == 0:
        print('Введите длину поля и число')
        count_symb = int(input())
        pos=bin(int(input()))[2:]
        field = createField(count_symb, pos)
        if field==0:
            print('Введите еще раз')
    while notrestart:

        print(field)
        command = input()
        count=1
        if len(command) > 1:
            count = int(command[2:])
        elif len(command) == 1:
            notrestart=False
        for i in range(count):
            field = step(field, count_symb)

