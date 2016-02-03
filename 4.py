import copy
import math

def requestField():
    field = None
    while field == None:
        print("Enter size of field and template")
        size = int(input())
        number = int(input())
        field = createField(size, number)
    return field

def createField(size, number):
    template = str(bin(number))[2:]
    if size < len(template):
        print("Template larger then field size! Try again.")
        return None

    digit_to_state = {'1': 'O', '0': '.'}
    field = ['.'] * size # изначально все клетки на поле мертвы
    len_difference = size - len(template)
    for i in range(len(template)):
        field[len_difference + i] = digit_to_state[template[i]]
    return field

def checkCell(field, i):
    # клетка жива только тогда, когда у нее 1 живой сосед, т.е. соседи разные
    return field[i - 1] != field[i + 1]

def main():
    field = requestField()

    while True:
        command = input()
        count = 1
        if command == '':
            count = 1
        if command == 'w':
            count = 10
        if command == 'r':
            field = requestField()

        print(''.join(field))
        for i in range(count):
            newField = copy.copy(field)

            # костыль для крайних клеток
            newField[0] = field[1]
            newField[-1] = field[-2]

            # проверка для всех остальных клеток
            for i in range(1, len(field) - 1):
                if checkCell(field, i):
                    newField[i] = 'O'
                else:
                    newField[i] = '.'

            field = copy.copy(newField)

    return 0

main()
