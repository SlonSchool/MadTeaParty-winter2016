def createField(count_symb, d):
    result = ['.' for i in range(count_symb)]
    log = 0
    max_log = 1;
    while max_log < count_symb:
        max_log *= d
        log += 1
    for i in [d ** n - 1 for n in range(0, log)]:
        result[i] = 'o'
    return ''.join(result)

def step(oldField, count_symb):
    oldField = '.' + oldField + '.' # Borders
    newField = []
    for i in range(1, count_symb):
        if (oldField[i + 1] == 'o') ^ (oldField[i - 1] == 'o'): # '^' means xor
            newField.append('o')
        else:
            newField.append('.')
    return ''.join(newField)

count_symb = int(input())
d = int(input())
field = createField(count_symb, d)
while True:
    print(field)
    step_count = input()
    if step_count == 'w':
        count = 10
    else:
        count = 1
    for i in range(count):
        field = step(field, count_symb)

