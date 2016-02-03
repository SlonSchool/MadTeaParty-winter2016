def createField():
    result = ['.' for i in range(200)]
    for i in [2 ** n - 1 for n in range(0, 7)]:
        result[i] = 'o'
    return ''.join(result)

def step(oldField):
    oldField = '.' + oldField + '.' # Borders
    newField = []
    for i in range(1, 200):
        if (oldField[i + 1] == 'o') ^ (oldField[i - 1] == 'o'): # '^' means xor
            newField.append('o')
        else:
            newField.append('.')
    return ''.join(newField)

field = createField()
while True:
    print(field)
    field = step(field)
    input()
