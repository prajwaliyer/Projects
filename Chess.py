from termcolor import colored


# FUNCTION TO MOVE PIECES
def move():

    x = 0
    y = 0
    i = 0
    j = 0

    i_move = str(input("Position of piece you would like to move: "))
    i_letter = i_move[0]
    i_number = i_move[1]

    o_move = str(input("Position you want to move piece to: "))
    o_letter = o_move[0]
    o_number = o_move[1]

    if i_letter == 'a':
        i = 1
    if i_letter == 'b':
        i = 2
    if i_letter == 'c':
        i = 3
    if i_letter == 'd':
        i = 4
    if i_letter == 'e':
        i = 5
    if i_letter == 'f':
        i = 6
    if i_letter == 'g':
        i = 7
    if i_letter == 'h':
        i = 8

    if i_number == '1':
        j = 1
    if i_number == '2':
        j = 2
    if i_number == '3':
        j = 3
    if i_number == '4':
        j = 4
    if i_number == '5':
        j = 5
    if i_number == '6':
        j = 6
    if i_number == '7':
        j = 7
    if i_number == '8':
        j = 8

    if o_letter == 'a':
        x = 1
    if o_letter == 'b':
        x = 2
    if o_letter == 'c':
        x = 3
    if o_letter == 'd':
        x = 4
    if o_letter == 'e':
        x = 5
    if o_letter == 'f':
        x = 6
    if o_letter == 'g':
        x = 7
    if o_letter == 'h':
        x = 8

    if o_number == '1':
        y = 1
    if o_number == '2':
        y = 2
    if o_number == '3':
        y = 3
    if o_number == '4':
        y = 4
    if o_number == '5':
        y = 5
    if o_number == '6':
        y = 6
    if o_number == '7':
        y = 7
    if o_number == '8':
        y = 8

    # FUNCTION TO VALIDATE MOVES
    def validate():

        global check

        # CHECKING FOR  BLUE TEAMMATES
        if board[j][i] == colored(' P ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                      board[y][x] == colored(' R ', 'blue') or
                                                      board[y][x] == colored(' N ', 'blue') or
                                                      board[y][x] == colored(' B ', 'blue') or
                                                      board[y][x] == colored(' Q ', 'blue') or
                                                      board[y][x] == colored(' K ', 'blue')):
            check = 0
        elif board[j][i] == colored(' R ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                        board[y][x] == colored(' R ', 'blue') or
                                                        board[y][x] == colored(' N ', 'blue') or
                                                        board[y][x] == colored(' B ', 'blue') or
                                                        board[y][x] == colored(' Q ', 'blue') or
                                                        board[y][x] == colored(' K ', 'blue')):
            check = 0
        elif board[j][i] == colored(' N ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                        board[y][x] == colored(' R ', 'blue') or
                                                        board[y][x] == colored(' N ', 'blue') or
                                                        board[y][x] == colored(' B ', 'blue') or
                                                        board[y][x] == colored(' Q ', 'blue') or
                                                        board[y][x] == colored(' K ', 'blue')):
            check = 0
        elif board[j][i] == colored(' B ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                        board[y][x] == colored(' R ', 'blue') or
                                                        board[y][x] == colored(' N ', 'blue') or
                                                        board[y][x] == colored(' B ', 'blue') or
                                                        board[y][x] == colored(' Q ', 'blue') or
                                                        board[y][x] == colored(' K ', 'blue')):
            check = 0
        elif board[j][i] == colored(' Q ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                        board[y][x] == colored(' R ', 'blue') or
                                                        board[y][x] == colored(' N ', 'blue') or
                                                        board[y][x] == colored(' B ', 'blue') or
                                                        board[y][x] == colored(' Q ', 'blue') or
                                                        board[y][x] == colored(' K ', 'blue')):
            check = 0
        elif board[j][i] == colored(' K ', 'blue') and (board[y][x] == colored(' P ', 'blue') or
                                                        board[y][x] == colored(' R ', 'blue') or
                                                        board[y][x] == colored(' N ', 'blue') or
                                                        board[y][x] == colored(' B ', 'blue') or
                                                        board[y][x] == colored(' Q ', 'blue') or
                                                        board[y][x] == colored(' K ', 'blue')):
            check = 0

        # CHECKING FOR  YELLOW TEAMMATES
        elif board[j][i] == colored(' P ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        elif board[j][i] == colored(' R ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        elif board[j][i] == colored(' N ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        elif board[j][i] == colored(' B ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        elif board[j][i] == colored(' Q ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        elif board[j][i] == colored(' K ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
                                                          board[y][x] == colored(' R ', 'yellow') or
                                                          board[y][x] == colored(' N ', 'yellow') or
                                                          board[y][x] == colored(' B ', 'yellow') or
                                                          board[y][x] == colored(' Q ', 'yellow') or
                                                          board[y][x] == colored(' K ', 'yellow')):
            check = 0
        # IF BOTH YELLOW AND BLUE AREN'T ATTACKING TEAM MATES
        else:
            check = 1

        # PAWN
        if board[j][i] == colored(' P ', 'blue'):
            if j == 2:
                if y == 3 or y == 4:
                    return 1
            elif board[y][x] != ' - ':
                if abs(x-i) == 1 and y-j == 1:
                    return 1
            elif board[y][x] == ' - ':
                if y-j == 1 and x-i == 0:
                    return 1
            else:
                return 0
        if board[j][i] == colored(' P ', 'yellow'):
            if j == 7:
                if y == 6 or y == 5:
                    return 1
            elif board[y][x] != ' - ':
                if abs(x-i) == 1 and j-y == 1:
                    return 1
            elif board[y][x] == ' - ':
                if j-y == 1 and x-i == 0:
                    return 1
            else:
                return 0

        # ROOK
        if board[j][i] == colored(" R ", 'blue') or board[j][i] == colored(" R ", 'yellow'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            else:
                return 0

        # KNIGHT
        if board[j][i] == colored(" N ", 'blue') or board[j][i] == colored(" N ", 'yellow'):
            if abs(y-j) == 2 and abs(x-i) == 1:
                return 1
            elif abs(x-i) == 2 and abs(y-j) == 1:
                return 1
            else:
                return 0

        # BISHOP
        if board[j][i] == colored(" B ", 'blue') or board[j][i] == colored(" B ", 'yellow'):
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # QUEEN
        if board[j][i] == colored(" Q ", 'blue') or board[j][i] == colored(" Q ", 'yellow'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # KING
        if board[j][i] == colored(" K ", 'blue') or board[j][i] == colored(" K ", 'yellow'):
            if abs(y-j) <= 1 and abs(x-i) <= 1:
                if abs(y-j) == 0 and abs(x-i) == 0:
                    return 0
                else:
                    return 1
            else:
                return 0

    # VALIDATING AND MOVING
    if validate() == 1 and check == 1:
        if board[y][x] == " - ":
            t = board[y][x]
            board[y][x] = board[j][i]
            board[j][i] = t
        else:
            board[y][x] = board[j][i]
            board[j][i] = ' - '
    else:
        print("Invalid move")


# MAIN FUNCTION
def main():
    global board
    board = [['  ', colored(' a ', 'red'), colored(' b ', 'red'), colored(' c ', 'red'),
             colored(' d ', 'red'), colored(' e ', 'red'), colored(' f ', 'red'),
             colored(' g ', 'red'), colored(' h ', 'red')],
             [colored('1 ', 'red'), colored(' R ', 'blue'), colored(' N ', 'blue'), colored(' B ', 'blue'),
             colored(' Q ', 'blue'), colored(' K ', 'blue'), colored(' B ', 'blue'),
             colored(' N ', 'blue'), colored(' R ', 'blue')],
             [colored('2 ', 'red'), colored(' P ', 'blue'), colored(' P ', 'blue'), colored(' P ', 'blue'),
             colored(' P ', 'blue'), colored(' P ', 'blue'), colored(' P ', 'blue'),
             colored(' P ', 'blue'), colored(' P ', 'blue')],
             [colored('3 ', 'red'), ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [colored('4 ', 'red'), ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [colored('5 ', 'red'), ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [colored('6 ', 'red'), ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [colored('7 ', 'red'), colored(' P ', 'yellow'), colored(' P ', 'yellow'), colored(' P ', 'yellow'),
             colored(' P ', 'yellow'), colored(' P ', 'yellow'), colored(' P ', 'yellow'), colored(' P ', 'yellow'),
             colored(' P ', 'yellow')],
             [colored('8 ', 'red'), colored(' R ', 'yellow'), colored(' N ', 'yellow'), colored(' B ', 'yellow'),
             colored(' Q ', 'yellow'), colored(' K ', 'yellow'), colored(' B ', 'yellow'), colored(' N ', 'yellow'),
             colored(' R ', 'yellow')]]

    for k in range(10):
        for j in range(9):
            for i in range(9):
                print(board[j][i], end='')
            print()
        move()


# CALLING MAIN FUNCTION
main()
