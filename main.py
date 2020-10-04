def paint():
    print("---------")
    print("| " + nested_lst[0][0] + " " + nested_lst[0][1] + " " + nested_lst[0][2] + " |")
    print("| " + nested_lst[1][0] + " " + nested_lst[1][1] + " " + nested_lst[1][2] + " |")
    print("| " + nested_lst[2][0] + " " + nested_lst[2][1] + " " + nested_lst[2][2] + " |")
    print("---------")


def get_result():
    global nested_lst
    counter = 0
    # horizontal x
    for i in range(3):
        counter = 0
        for j in range(3):
            if nested_lst[i][j] == 'X':
                counter += 1
                if counter == 3:
                    paint()
                    print("X wins")
                    return True
            else:
                counter = 0
    # vertical x
    for i in range(3):
        counter = 0
        for j in range(3):
            if nested_lst[j][i] == 'X':
                counter += 1
                if counter == 3:
                    paint()
                    print("X wins")
                    return True
            else:
                counter = 0
    # horizontal o
    for i in range(3):
        counter = 0
        for j in range(3):
            if nested_lst[i][j] == 'O':
                counter += 1
                if counter == 3:
                    paint()
                    print("O wins")
                    return True
            else:
                counter = 0
    # vertical o
    for i in range(3):
        counter = 0
        for j in range(3):
            if nested_lst[j][i] == 'O':
                counter += 1
                if counter == 3:
                    paint()
                    print("O wins")
                    return True
            else:
                counter = 0
    # diagonal x
    if nested_lst[0][0] == 'X' and nested_lst[1][1] == 'X' and nested_lst[2][2] == 'X':
        paint()
        print("X wins")
        return True
    if nested_lst[0][2] == 'X' and nested_lst[1][1] == 'X' and nested_lst[2][0] == 'X':
        paint()
        print("X wins")
        return True
    # diagonal o
    if nested_lst[0][0] == 'O' and nested_lst[1][1] == 'O' and nested_lst[2][2] == 'O':
        paint()
        print("O wins")
        return True
    if nested_lst[0][2] == 'O' and nested_lst[1][1] == 'O' and nested_lst[2][0] == 'O':
        paint()
        print("O wins")
        return True
    # draw
    counter = 0
    for i in range(3):
        for j in range(3):
            if nested_lst[i][j] == " ":
                counter += 1
    if counter == 0:
        paint()
        print("Draw")
        return True
    # not finished
    return False


finished = False
nested_lst = []
for i in range(3):
    nested_lst.append([])
    for j in range(3):
        nested_lst[i].append(" ")
move = 0
paint()
while not finished:
    x, y = input("Enter the coordinates: ").split()
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("You should enter numbers!")
        continue
    if x > 3 or x < 1 or y > 3 or x < 1:
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        x = abs(x - 1)
        y = abs(y - 3)
        if nested_lst[y][x] == ' ':
            if move % 2 == 0:
                nested_lst[y][x] = 'X'
            else:
                nested_lst[y][x] = 'O'
            move += 1
            finished = get_result()
            if finished:
                break
            paint()
        else:
            print("This cell is occupied! Choose another one!")