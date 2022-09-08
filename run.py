import random

# created a function to use in if else statements
def line():
    print('-----------------------------------')


line()
print('Welcome to the Sea Battleship game.')
line()
print('Find and destroy all the hidden ships on board.')
line()
print('You have ** 8 ** bullets and there are ** 2 ** hidden ships on board.')
line()

# Board for holding ship locations
def new_game():
    board = [['O', 'O', 'O', 'O', ],
             ['O', 'O', 'O', 'O', ],
             ['O', 'O', 'O', 'O', ],
             ['O', 'O', 'O', 'O', ]]

    for a in board:
        print(*a)
        # created random ship function
        def random_ship():
            return random.randrange(row), random.randrange(column)
        row = 4
        column = 4

    ship1 = random_ship()
    ship2 = random_ship()
    ships_left = 2
    bullets = 8

    while bullets:
        try:
            line()
            row = int(input('Guess a row number between 0-3:\n '))
            column = int(input('Guess a column number between 0-3:\n '))
        except ValueError:
            print('*You must enter a number!*')
            continue

        if (row < 0 or row > 3) or (column < 0 or column > 3):
            print('*Numbers must be between 0-3!*')
            continue

        if board[row][column] == '-' or board[row][column] == 'X':
            line()
            print('*You guessed that one already*')
            line()
            continue

        elif (row, column) == ship1 or (row, column) == ship2:
            line()
            print('*You hit a ship, You got one extra bullet!*')
            line()
            board[row][column] = 'X'
            ships_left -= 1
            if ships_left == 0:
                line()
                print('*Congratulations, You destroy all ships*')
                play_again()
        else:
            print('-------------')
            print('*You missed!*')
            print('-------------')
            board[row][column] = '-'
            bullets -= 1

        for a in board:
            print(*a)
        line()
        print(f'bullets left:{bullets}. Ships left:{ships_left}. on board.')

    play_again()

# Game play again function
def play_again():
    try_again = input('Try again? (Y/N):\n')
    if try_again.lower() == 'y':
        line()
        new_game()
    else:
        print('Game Over')
        return


if __name__ == '__main__':
    new_game()
