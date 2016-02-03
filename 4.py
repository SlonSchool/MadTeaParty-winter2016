import copy
import math

def createField(size, d):
    field = ['.'] * size # изначально все клетки на поле мертвы
    for i in range(int(math.log(size, d)) + 1):
        field[d ** i - 1] = 'O' # клетки с номерами степеней d (нумерация с нуля) становятся живыми
    return field

def main():
    size = int(input())
    d = int(input())
    field = createField(size, d)

    print(''.join(field))

    while True:
        # ожидание нажатия энтера
        waiting = input()

        count = 1
        if waiting == 'w':
            count = 10

        for i in range(count):
            newField = copy.copy(field)

            # костыль для крайних клеток
            newField[0] = field[1]
            newField[-2] = field[-1]

            # проверка для всех остальных клеток
            # клетка жива только тогда, когда у нее 1 живой сосед, т.е. соседи разные
            for i in range(1, len(field) - 1):
                if field[i - 1] != field[i + 1]:
                    newField[i] = 'O'
                else:
                    newField[i] = '.'

            field = copy.copy(newField)

        print(''.join(field))

    return 0

main()
