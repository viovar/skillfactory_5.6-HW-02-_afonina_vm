def table():
    print (f" 0 1 2")
    for i in range (3):
        row=" ".join(field[i])
        print(f"{i} {row}")

def ask():
    while True:
        cords = input("Ваш ход").split()
        if len(cords) != 2:
            print ("Введите координаты хода")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Надо вводить числа ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Неверный ход")
            continue
        if field[x][y] != " ":
            print ("Занято")
            continue
        return x, y
def winner():
    win_1 = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,2),(1,1),(2,0)),((0,0),(1,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)))
    for w in win_1:
        b = []
        for n in w:
            b.append(field[n[0]][n[1]])
        if b == ["x","x","x"]:
            print ("Победа X")
            return True
        if b == ["0","0","0"]:
            print ("Победа 0")
            return True
    return False

field=[[" "]*3 for i in range(3)]
count=0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = ask()
    if count %2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"
    if winner():
        break
    if count == 9:
        print("Ничья")
        break
