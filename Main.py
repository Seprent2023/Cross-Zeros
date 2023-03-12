game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (2, 4, 7), (2, 6, 8),
             (0, 4, 8), (2, 4, 6)]


def draw_board(game):
    print("-" * 13)
    for i in range(3):
        print("|", game[0 + i * 3], "|", game[1 + i * 3], "|", game[2 + i * 3], "|")
        print("-" * 13)


def coord():
    game_coord = input("Введите координату для хода (число от 0 до 8, слева на право, сверху вниз): ")
    if game_coord.isdigit():
        game_coord = int(game_coord)
        if 8 < game_coord:
            print("Координата выходит за пределы поля! Введите число от 0 до 8!")
            coord()
        elif game[game_coord] == "X" or game[game_coord] == "O":
            print("Ячейка занята, пожалуйств выберите другую координату")
            coord()
        else:
            return game_coord
    else:
        print("Неверный формат! Введите число от 0 до 8!")
        coord()


def move(coordinate):
    game[coordinate] = input("Сделайте свой ход: ").upper()
    game[coordinate].upper()
    if num % 2 == 1 and game[coordinate] == "X":
        return game
    elif num % 2 == 1 and not game[coordinate] == "X":
        print("Неверный формат! Должны ходить КРЕСТИКИ! Введите букву Х на английской раскладке!")
        move(coordinate)
    elif num % 2 == 0 and game[coordinate] == "O":
        return game
    elif num % 2 == 0 and not game[coordinate] == "O":
        print("Неверный формат! Должны ходить НОЛИКИ! Введите букву О на английской раскладке!")
        move(coordinate)


def win_check():
    for c in win_coord:
        a, b, c = c[0], c[1], c[2]
        if game[a] == 'X' and game[b] == 'X' and game[c] == 'X':
            print("Выйграли КРЕСТИКИ!!!")
            return True
        if game[a] == 'O' and game[b] == 'O' and game[c] == 'O':
            print("Выйграли НОЛИКИ!!!")
            return True
    return False


num = 0
while True:
    num += 1
    draw_board(game)
    if num % 2 == 1:
        print("Ход КРЕСТИКОВ")
    else:
        print("Ход НОЛИКОВ")
    coordinate = coord()
    move(coordinate)
    if win_check():
        break
    if num == 9:
        print("Увы, ничья...")
        break
