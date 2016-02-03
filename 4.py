import copy

def check_cell(field, index):
    # клетка жива только тогда, когда у нее 1 живой сосед, т.е. соседи разные
    return field[i - 1] != field[i + 1]

def main():
    field = ['.'] * 200 # изначально все клетки на поле мертвы
    for i in range(0, 8):
        field[2 ** i - 1] = 'O' # клетки с номерами степеней двойки (нумерация с нуля) становятся живыми

    while True:
        print(''.join(field))
        # ожидание нажатия энтера
        waiting = input()

        newField = copy.copy(field)

        # костыль для крайних клеток
        newField[0] = field[1]
        newField[-2] = field[-1]

        # проверка для всех остальных клеток
        for i in range(1, len(field) - 1):
            if check_cell(field, i):
                newField[i] = 'O'
            else:
                newField[i] = '.'

        field = newField

    return 0

main()
