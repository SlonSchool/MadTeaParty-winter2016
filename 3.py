def check(live, fieldSize):
    return fieldSize >= len(bin(live)) - 2

def generate_field():
    fieldSize = int(input('Введите размер поля \n'))
    live = int(input('Введите десятичное число, соответствующее полю \n'))

    while not check(live, fieldSize):
        print('не корректный ввод')
        fieldSize = int(input('Введите размер поля \n'))
        live = int(input('Введите десятичное число, соответствующее полю \n'))

    pole = bin(live)[2:]
    field = ['.'] * (fieldSize - len(pole))
    for i in pole:
        if i == '1':
            field.append('o')
        else:
            field.append('.')
    return field

def lifeIteration():
    j=[]
    m=[]
    if field[1]=='.':
        m.append(0)
    else:
        j.append(0)
    n=len(field)
    if field[n-2]=='.':
        m.append(n-1)
    else:
        j.append(n-1)
    for i in range(1, n-1):
        if (field[i-1]=='.' and field[i+1]=='.') or (field[i-1]=='o' and field[i+1]=='o'):
            m.append(i)
        else:
            j.append(i)
    for i in j:
        field[i]='o'
    for i in m:
        field[i]='.'




field = generate_field()

while True:
    print(''.join(field))
    action = input()
    if action == 'w':
        for i in range(10):
            lifeIteration()
    elif action == 'r':
        field = generate_field()
    else:
        lifeIteration()
