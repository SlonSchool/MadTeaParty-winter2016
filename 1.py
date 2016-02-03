from copy import deepcopy


print("Enter field length")
amount = int(input())
print("Enter d - geom increment")
degree = int(input())

live = ['.'] * (amount + 1)
cord = 1
while True:
    live[cord] = 'o'
    cord *= degree
    if cord > amount:
        break
live = live[1:]
live = ['.'] + live + ['.']


print("".join(live[1:-1]))

while True:
    s = input()
    steps_to_pass = 0
    if s == "":
        steps_to_pass = 1
    if s == "w":
        steps_to_pass = 10

    for step in range(steps_to_pass):
        new = []
        for i in range(1, len(live) - 1):
            if live[i - 1] == 'o' and live[i + 1] == 'o' or live[i - 1] != 'o' and live[i + 1] != 'o':
                new.append('.')
            else:
                new.append('o')
        live = deepcopy(new)
        live = ['.'] + new + ['.']

    print("".join(live[1:-1]))

