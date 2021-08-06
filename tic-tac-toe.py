import time
import random

def draw_game_board():
#Рисует игровое поле: пустое, если еще не сделано ходов.
    game_board = f"""
____________
|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|
____________"""
#так выглядит поле по дефолту, если ходов еще не сделано
    for i in range(1, 10):
#проходим по всем элементам строки, кроме [0] (чтобы позиция в строке совпадала с номером в клетке на доски, иначе всё будет смещено на 1 элемент
        if game_state[i] == 'X' or game_state[i] == 'O':
#если видим, что в этом поле стоит Х или О, то:
            game_board = game_board.replace(str(i), game_state[i])
#заменяем цифру в клетке на поле на содержимое строки с состоянием игры по индексу [i]
    print(game_board)
#выводим получившееся игровое поле на экран

def player_selection():
#игроки выбирают, кем будут играть
    player1, player2 = None, None
#сначала обнуляем выбор
    while player1 != 'X' and player1 != 'O':
#пока игрок не выберет Х или О, цикл будет просить выбрать
        player1 = input('Player 1: choose X or O ').upper()
#сразу конвертируем input в uppercase
    if player1 == 'X':
#если первый выбрал Х, то второй игрок будет О
        player2 = 'O'
    else:
#если первый выбрал О, то второй будет Х
        player2 = 'X'
    print(f'Player 1 is {player1}, Player 2 is {player2}')
#сообщаем игрокам, за кого они играют
    return player1, player2
#возвращаем выбор игроков, чтобы использовать его дальше в программе

def move(player, position, game_state):
#берет символ игрока (Х или О), ход, который он хочет сделать, состояние поля
    game_state[position] = player
#записывает символ игрока в строку с состоянием поля под индексом, который передали в аргументах
    return game_state
#возвращает новое состояние поля

def board_not_full(game_state):
#Проверяет, что на поле есть место
    return game_state.count('*') > 1
#Если в строке с состоянием поля остался только один символ, который мы используем как плейсхолдер, значит на поле нет места

def allowed_move(game_state, position):
#проверяет, допустим ли ход на выбранную клетку, исходя из состяния поля, и возвращает True, если такой ход возможен и False, если нет
    if position < 1 or position > 9:
#проверка, что игрок вводит цифру от 1 до 9
        print('You need to pick a number between 1 and 9')
        return False
    if game_state[position] != '*':
#проверяет, что в списке с состоянием поля это место еще не занято
        print('This square is occupied, pick another:')
        return False
    else:
        return True

def turn(player, game_state):
#Отрабатывает ход игрока, принимает номер игрока и состояние поля в качестве аргумента
    position = int(input(f"{player}, it's your turn. Pick a square "))
#Спрашивает игрока, куда поставить его Х или О
    while not allowed_move(game_state, position):
#Просит сделать ход до тех пор, пока игрок не сделает корректный ход
        position = int(input(f"{player}, it's your turn. Pick a square "))
    move(player, position, game_state)
#обновляет состояние поля
    draw_game_board()
#рисует обновленное поле

def toss_a_coin():
#выбирает, чей ход будет первый
    print('Deciding, who goes first')
#это и дальше не несет смысловой нагрузки, просто для развлечения
    for i in range(3):
        print('Still deciding...')
        time.sleep(1)
    if random.randrange(1, 1000) % 2 == 0:
#рандомно решает, кто будет ходить
        print('Player 1 goes first')
        return 0
#возвращает в программу значение, которое указывает, чей ход первый
    else:
        print('Player 2 goes first')
        return 1

def game_over_win(game_state, player):
#здесь проверяются условия победы: не стоят ли в ряд три одинаковых символа для игрока, который передан в качестве аргумента
    if game_state[1] == game_state[2] == game_state [3] == player:
        return True
    elif game_state[4] == game_state[5] == game_state [6] == player:
        return True
    elif game_state[7] == game_state[8] == game_state [9] == player:
        return True
    elif game_state[1] == game_state[4] == game_state [7] == player:
        return True
    elif game_state[2] == game_state[5] == game_state [8] == player:
        return True
    elif game_state[3] == game_state[6] == game_state [9] == player:
        return True
    elif game_state[1] == game_state[5] == game_state [9] == player:
        return True
    elif game_state[3] == game_state[5] == game_state [7] == player:
        return True
    else:
        return False

def game_loop():
#Чей первый ход, здесь просто создаем переменную
    player1, player2 = player_selection()
#распределяем, кто Х, а кто О
    time.sleep(2)
#чтобы строки не мелькали слишком быстро
    pendulum = toss_a_coin() + 1
#это «маятник», который определяет порядок ходов
#если маятник в нечетном положении, то ходит игрок 1, если в четном — игрок 2
#если жребьевку выиграл игрок 2, то смещаем маятник на 1, чтобы начать цикл из четного положения
    time.sleep(2)
    draw_game_board()
#рисуем пустое поле

    while board_not_full(game_state):
#создаем цикл, который крутится, пока на поле есть место или пока кто-то не победит
        if pendulum % 2 != 0:
#если первым ходит игрок 1, то порядок ходов такой
            turn(player1, game_state) #отрабатываем ход игроков по очереди
            pendulum += 1
#двигаем маятник в сторону второго игрока
            if game_over_win(game_state, player1):
#если наступило условие победы, прекращаем цикл
                print(f'Player 1 ({player1}) wins!')
                break
        else:
#здесь обрабатывается ход второго игрока, в остальном все аналогично игроку 1
            turn(player2, game_state)
            pendulum += 1
            if game_over_win(game_state, player2):
                print(f'Player 2 ({player2}) wins!')
                break
    print('Game over')

while True:
    print('WELCOME TO TIC-TAC-TOE!!!!111 \n*** *** ***')
    run_the_game = None
    while run_the_game != 'Y' and run_the_game != 'N':
#Цикл, который работает, пока игрок отвечает, что хочет играть
        run_the_game = input('Do you want to play a game? (Y/N): ').upper()
    if run_the_game == 'Y':
        game_state = ['*'] * 10
#создает список из десяти элементов, чтобы хранить в нём ходы игроков
        game_loop()
#запускаем основную часть игры
    else:
        print('Bye! Have a great day.')
        break

    


