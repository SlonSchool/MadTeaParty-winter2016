import copy
import math

ALIVE = 'O'
DEAD = '.'

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

    digit_to_state = {'1': ALIVE, '0': DEAD}
    field = [DEAD] * size # изначально все клетки на поле мертвы
    len_difference = size - len(template)
    for i in range(len(template)):
        field[len_difference + i] = digit_to_state[template[i]]
    return field

def checkCell(field, i):
    # клетка выживает если жив ровно один сосед                 или если она была мертва, а слева есть живой
    return (field[i - 1] != field[i + 1] and field[i] == ALIVE) or (field[i - 1] == ALIVE and field[i] == DEAD)

def updated(field):
    newField = copy.copy(field)
    field = [DEAD] + field + [DEAD]
    # проверка для всех остальных клеток
    for i in range(1, len(field) - 1):
        if checkCell(field, i):
            newField[i - 1] = ALIVE
        else:
            newField[i - 1] = DEAD
    return newField


def main():
    field = requestField()

    while True:
        print(''.join(field))
        command = input()
        count = 1
        if command == '':
            count = 1
        if command == 'w':
            count = int(input('Enter count of steps: '))
        if command == 'r':
            field = requestField()
        for i in range(count):
            field = updated(field)

main()
