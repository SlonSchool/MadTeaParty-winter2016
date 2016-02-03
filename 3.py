fieldSize = int(input('Введите размер поля \n'))
d = int(input('Введите коэффициент геометрической прогрессии \n'))

field=[]
for i in range(fieldSize):
    field.append('.')

# оживление клеток с нужными номерами
number=1
while number<fieldSize:
    field[number-1]='o'
    number*=d

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

while True:
    print(''.join(field))
    h=input()
    if h == 'w':
        for i in range(10):
            lifeIteration()
    else:
        lifeIteration()
