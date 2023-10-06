# Псевдо очистка экрана
def cls():
    print("\n" * 20)


# Заголовок + правила
print("-------------------------------")
print("    Игра крестики - нолики")
print("-------------------------------")
print("Для игры требуются 2 игрока")
print("Игроки по очереди ставят X или O")
print("в свободное поле.")
print("При заполнении 3х одинаковых символов подряд")
print("в любом направлении игрок - побеждает.")

# Запроcим имена игроков
Player1 = input("X: Имя 1го игрока: ")
Player2 = input("O: Имя 2го игрока: ")

# Можно в принципе запросить любой размер поля от 3 до 9
max_x = 3
max_y = 3


def create_area(x, y):
    result = []
    for iy in range(y):
        res_x = []
        for ix in range(x):
            res_x.append("-")
        result.append(res_x)
    return result


# Вывод поля
def print_area(x, y):
    for iy in range(y + 1):
        str_ = ""
        for ix in range(x + 1):
            if iy == 0:
                str_ = str_ + (" " if ix == 0 else " " + str(ix)) + (" X" if ix == x else "")
            else:
                str_ = str_ + (str(iy) if ix == 0 else " " + area[iy - 1][ix - 1])
        print(str_)
    print("Y")


def check_win(simvol):
    result = False
    for y in range(max_y):
        for x in range(max_x):
            a_ = area[y]
            if (x + 2 <= max_x - 1 and y + 2 <= max_y - 1) and all(
                    [area[y][x] == simvol, area[y + 1][x + 1] == simvol, area[y + 2][x + 2] == simvol]):
                result = True
            elif (0 <= x - 2 and y + 2 <= max_y - 1) and all(
                    [area[y][x] == simvol, area[y + 1][x - 1] == simvol, area[y + 1][x - 2] == simvol]):
                result = True
            elif (x + 2 <= max_x - 1 and y - 2 <= max_y - 1) and all(
                    [area[y][x] == simvol, area[y - 1][x + 1] == simvol, area[y - 2][x + 2] == simvol]):
                result = True
            elif (0 <= x - 2 and y - 2 <= max_y - 1) and all(
                    [area[y][x] == simvol, area[y - 1][x - 1] == simvol, area[y - 2][x - 2] == simvol]):
                result = True
            elif x + 2 <= max_x - 1 and all(
                    [area[y][x] == simvol, area[y][x + 1] == simvol, area[y][x + 2] == simvol]):
                result = True
            elif 0 <= x - 2 and all([area[y][x] == simvol, area[y][x - 1] == simvol, area[y][x - 2] == simvol]):
                result = True
            elif y + 2 <= max_y - 1 and all([area[y][x] == simvol, area[y + 1][x] == simvol, area[y + 2][x] == simvol]):
                result = True
            elif 0 <= y - 2 and all([area[y][x] == simvol, area[y - 1][x] == simvol, area[y - 2][x] == simvol]):
                result = True
    return result


area = create_area(max_x, max_y)
hod = 0
error_ = ""
while True:
    cls()
    print_area(max_x, max_y)

    win_ = check_win("X" if not hod else "O")
    # error_ = win_

    if win_:
        print("Поздравляем, победил: %s" % (Player1 if not hod else Player2))
        break
    else:
        # Проверим все ли клетки заполнены
        full_ = True
        for ch_y in range(max_y):
            if "-" in area[ch_y]:
                full_ = False
                break
        if full_:
            print("Все поля заняты, ничья")
            break

    if error_ != "":
        print("---", error_, "---")
    else:
        print("")
    error_ = ""

    if hod:
        xy = input("X: Ход игрока %s, введите XY, 0 - прервать: " % Player1)
    else:
        xy = input("O: Ход игрока %s, введите XY, 0 - прервать: " % Player2)

    if xy == "0":
        print("Завершение игры. Спасибо что играли")
        break

    # Проверим введено ли нужные координаты
    if not xy.isnumeric():
        error_ = "Вводите только числа"
        continue
    if xy == "": continue
    if len(xy) != 2:
        error_ = "Введите координаты в формате XY"
        continue

    xx, yy = int(xy[0]), int(xy[1])
    # Проверим входят ли координаты в доступные
    if any([xx < 1, xx > max_x, yy < 1, yy > max_y]):
        error_ = "Координаты выходят за доступный диапазон"
        continue

    # Проставляем символ на поле, если он свободен
    if area[yy - 1][xx - 1] != "-":
        error_ = "Клетка занята"
        continue
    else:
        area[yy - 1][xx - 1] = "X" if hod else "O"

    # Переход хода
    hod = not hod
