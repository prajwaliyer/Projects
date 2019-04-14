from termcolor import colored


# FUNCTION TO MOVE BLUE PIECES
def blue_move():

    global color_check
    global invalid

    x = 0
    y = 0
    i = 0
    j = 0

    i_move = str(input(colored("\nBLUE start position: ", 'blue')))
    i_letter = i_move[0]
    i_number = i_move[1]

    o_move = str(input(colored("BLUE end position  : ", 'blue')))
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

    # CHECKS IF SELECTED PIECE IS BLUE
    if board[j][i] == colored(' P ', 'blue'):
        color_check = 1
    elif board[j][i] == colored(' R ', 'blue'):
        color_check = 1
    elif board[j][i] == colored(' N ', 'blue'):
        color_check = 1
    elif board[j][i] == colored(' B ', 'blue'):
        color_check = 1
    elif board[j][i] == colored(' Q ', 'blue'):
        color_check = 1
    elif board[j][i] == colored(' K ', 'blue'):
        color_check = 1
    else:
        color_check = 0

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

        # IF BLUE ISN'T ATTACKING TEAM MATES
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

        # ROOK
        if board[j][i] == colored(" R ", 'blue'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            else:
                return 0

        # KNIGHT
        if board[j][i] == colored(" N ", 'blue'):
            if abs(y-j) == 2 and abs(x-i) == 1:
                return 1
            elif abs(x-i) == 2 and abs(y-j) == 1:
                return 1
            else:
                return 0

        # BISHOP
        if board[j][i] == colored(" B ", 'blue'):
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # QUEEN
        if board[j][i] == colored(" Q ", 'blue'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # KING
        if board[j][i] == colored(" K ", 'blue'):
            if abs(y-j) <= 1 and abs(x-i) <= 1:
                if abs(y-j) == 0 and abs(x-i) == 0:
                    return 0
                else:
                    return 1
            else:
                return 0

    # VALIDATING AND MOVING
    if validate() == 1 and check == 1 and color_check:
        if board[y][x] == " - ":
            t = board[y][x]
            board[y][x] = board[j][i]
            board[j][i] = t
            invalid = 1
        else:
            board[y][x] = board[j][i]
            board[j][i] = ' - '
            invalid = 1
    else:
        print("Invalid move")
        invalid = 0


# FUNCTION TO MOVE YELLOW PIECES
def yellow_move():

    global color_check
    global invalid

    x = 0
    y = 0
    i = 0
    j = 0

    i_move = str(input(colored("\nYELLOW start position: ", 'yellow')))
    i_letter = i_move[0]
    i_number = i_move[1]

    o_move = str(input(colored("YELLOW end position  : ", 'yellow')))
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

    # CHECKS IF SELECTED PIECE IS YELLOW
    if board[j][i] == colored(' P ', 'yellow'):
        color_check = 1
    elif board[j][i] == colored(' R ', 'yellow'):
        color_check = 1
    elif board[j][i] == colored(' N ', 'yellow'):
        color_check = 1
    elif board[j][i] == colored(' B ', 'yellow'):
        color_check = 1
    elif board[j][i] == colored(' Q ', 'yellow'):
        color_check = 1
    elif board[j][i] == colored(' K ', 'yellow'):
        color_check = 1
    else:
        color_check = 0

    # FUNCTION TO VALIDATE MOVES
    def validate():

        global check

        # CHECKING FOR  YELLOW TEAMMATES
        if board[j][i] == colored(' P ', 'yellow') and (board[y][x] == colored(' P ', 'yellow') or
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
        # IF YELLOW ISN'T ATTACKING TEAM MATES
        else:
            check = 1

        # PAWN
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
        if board[j][i] == colored(" R ", 'yellow'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            else:
                return 0

        # KNIGHT
        if board[j][i] == colored(" N ", 'yellow'):
            if abs(y-j) == 2 and abs(x-i) == 1:
                return 1
            elif abs(x-i) == 2 and abs(y-j) == 1:
                return 1
            else:
                return 0

        # BISHOP
        if board[j][i] == colored(" B ", 'yellow'):
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # QUEEN
        if board[j][i] == colored(" Q ", 'yellow'):
            if abs(y-j) != 0 and x-i == 0:
                return 1
            elif abs(x-i) != 0 and y-j == 0:
                return 1
            if abs(y-j) == abs(x-i):
                return 1
            else:
                return 0

        # KING
        if board[j][i] == colored(" K ", 'yellow'):
            if abs(y-j) <= 1 and abs(x-i) <= 1:
                if abs(y-j) == 0 and abs(x-i) == 0:
                    return 0
                else:
                    return 1
            else:
                return 0

    # VALIDATING AND MOVING
    if validate() == 1 and check == 1 and color_check == 1:
        if board[y][x] == " - ":
            t = board[y][x]
            board[y][x] = board[j][i]
            board[j][i] = t
            invalid = 1
        else:
            board[y][x] = board[j][i]
            board[j][i] = ' - '
            invalid = 1
    else:
        print("Invalid move")
        invalid = 0


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

    # THIS LOOP WILL RUN 1000 TIMES
    # IT PRINTS THE BOARD 1000 TIMES AND GIVES 500 TURNS TO EACH TEAM
    # TO BE CHANGED WHEN CHECK AND CHECKMATE ARE ADDED ...
    for k in range(1000):

        for j in range(9):
            for i in range(9):
                print(board[j][i], end='')
            print()
        yellow_move()
        # IF THE MOVE IS INVALID, THIS WILL REPEAT YELLOW'S TURN
        if invalid == 0:
            while invalid == 0:
                for j in range(9):
                    for i in range(9):
                        print(board[j][i], end='')
                    print()
                yellow_move()

        for j in range(9):
            for i in range(9):
                print(board[j][i], end='')
            print()
        blue_move()
        # IF THE MOVE IS INVALID, THIS WILL REPEAT BLUE'S TURN
        if invalid == 0:
            while invalid == 0:
                for j in range(9):
                    for i in range(9):
                        print(board[j][i], end='')
                    print()
                blue_move()


# CALLING MAIN FUNCTION
main()
