spisok = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

num = 1

for x in range( len(spisok)):
    if x+1!=10:
        print(x + 1, ") ",end='')
    else:
        print(x + 1, ")", end='')
    for y in range( len(spisok[x])):
        if spisok[x][y] == 1:
            print("⬛", end='')
        else:
            print("◻", end='')
    print()

