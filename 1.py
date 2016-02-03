from copy import deepcopy

LIVE_SIZE = 200

live = ['.'] * LIVE_SIZE
cord = 1
while cord <= LIVE_SIZE:
    live[cord-1] = 'o'
    cord *= 2

while True:
    print("".join(live))
    input()

    live = ['.'] + new + ['.']
    new_live = []
    for i in range(1, len(live) - 1):
        if (
            (live[i - 1] == 'o' and live[i + 1] == 'o')
            or (live[i - 1] != 'o' and live[i + 1] != 'o')
        ):
            new_live.append('.')
        else:
            new_live.append('o')
    live = deepcopy(new_live)


