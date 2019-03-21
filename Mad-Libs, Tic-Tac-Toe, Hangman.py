import time


# ----------------------------------------------------------------------------------------------------------------------
# MAD-LIBS
def mad_libs():
    print("\nThis is a mad-lib game. Input the details and the program will utilize them to make funny sentences.\n")
    name = input("Input male name: ")
    city = input("Input city: ")
    color = input("Input color: ")
    verb = input("Input -ing verb: ")
    food = input("Input plural food: ")
    number = input("Input number: ")
    years = int(input("Input years: "))
    months = (12 * years)

    print()
    print(name, " went to ", city, " ", months, " years ago.\n", "Back in 1880, he would be there every week.", sep='')
    print("If you ever saw him in ", city, ", you would find him ", verb, " all the time.", sep='')
    print("One day, a person saw him eating ", number, " ", color, " ", food, " and asked him for some.", sep='')
    print("But ", name, " said no. He said he would give some only if the person did ", number, " push ups.", sep='')
    time.sleep(10)


# ----------------------------------------------------------------------------------------------------------------------
# TIC-TAC-TOE
def tic_tac_toe():
    print("\nThis is a two-player Tic-Tac-Toe game.")
    print("Grab a friend!\n")
    number = ['   1   ', '   2   ', '   3   ', '   4   ', '   5   ', '   6   ', '   7   ', '   8   ', '   9   ']
    board = ['       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ']

    def x():                                                                                     # Let's the X user play

        pos = int(input("\nInput position you want to insert X in [1-9]: "))

        if pos == 1:
            board[0] = "   X   "
        if pos == 2:
            board[1] = "   X   "
        if pos == 3:
            board[2] = "   X   "
        if pos == 4:
            board[3] = "   X   "
        if pos == 5:
            board[4] = "   X   "
        if pos == 6:
            board[5] = "   X   "
        if pos == 7:
            board[6] = "   X   "
        if pos == 8:
            board[7] = "   X   "
        if pos == 9:
            board[8] = "   X   "

        print(board[0:3])
        print(board[3:6])
        print(board[6:9])

    def o():                                                                                     # Let's the O user play

        pos = int(input("\nInput position you want to insert O in [1-9]: "))

        if pos == 1:
            board[0] = "   O   "
        if pos == 2:
            board[1] = "   O   "
        if pos == 3:
            board[2] = "   O   "
        if pos == 4:
            board[3] = "   O   "
        if pos == 5:
            board[4] = "   O   "
        if pos == 6:
            board[5] = "   O   "
        if pos == 7:
            board[6] = "   O   "
        if pos == 8:
            board[7] = "   O   "
        if pos == 9:
            board[8] = "   O   "

        print(board[0:3])
        print(board[3:6])
        print(board[6:9])

    def winner():                       # Checks if anyone has won yet by checking all the possible victory combinations
        global win
        win = 0

        if board[0] == "   X   " and board[1] == "   X   " and board[2] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[3] == "   X   " and board[4] == "   X   " and board[5] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[6] == "   X   " and board[7] == "   X   " and board[8] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[0] == "   X   " and board[3] == "   X   " and board[6] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[1] == "   X   " and board[4] == "   X   " and board[7] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[2] == "   X   " and board[5] == "   X   " and board[8] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[0] == "   X   " and board[4] == "   X   " and board[8] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1
        if board[2] == "   X   " and board[4] == "   X   " and board[6] == "   X   ":
            print("\n\nX wins!")
            time.sleep(3)
            win = 1

        if board[0] == "   O   " and board[1] == "   O   " and board[2] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[3] == "   O   " and board[4] == "   O   " and board[5] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[6] == "   O   " and board[7] == "   O   " and board[8] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[0] == "   O   " and board[3] == "   O   " and board[6] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[1] == "   O   " and board[4] == "   O   " and board[7] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[2] == "   O   " and board[5] == "   O   " and board[8] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[0] == "   O   " and board[4] == "   O   " and board[8] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1
        if board[2] == "   O   " and board[4] == "   O   " and board[6] == "   O   ":
            print("\n\nO wins!")
            time.sleep(3)
            win = 1

    def play():                                                              # Calls in other functions to play the game
        for i in range(4):
            x()                                                                                               # X's turn
            winner()                                                                                    # Checks for win
            if win == 1:                                                         # If a winner is found, the loop breaks
                break
            o()                                                                                               # O's turn
            winner()                                                                                 # Checks for winner
            if win == 1:                                                         # If a winner is found, the loop breaks
                break
        if win == 0:                                               # If no one has one till the last turn, X plays again
            x()
            winner()

    print("\nThese are the positions of the board. They will be replaced by blanks after the first turn.")
    print(number[0:3])
    print(number[3:6])
    print(number[6:9])

    play()
    if win == 0:                                                                                        # Checks for tie
        print("\n\nTie!")
        time.sleep(3)


# ----------------------------------------------------------------------------------------------------------------------
# HANGMAN
def hangman():
    print("\nThis is a two-player hangman game. One player inputs a word and the other player guesses it.")
    print("Grab a friend!\n")

    word = input("\nTell your friend to input a word and press Enter key: ")
    word = word.upper()                                                                 # To avoid case sensitive errors
    print("\n\n\n\n\n\n\n\n\n\n\n")

    guess_word = ["_"] * len(word)                                        # The blank word in which letters are inserted

    word_guess_word = ''                                        # Will be used to convert the word from list into string

    directory = []                                      # Stores letters which have been used to avoid repeating letters

    trial = 0                                                                                         # Number of trials

    over = 0                                                   # Will be used to end the loop once word is fully guessed

    while trial < 6 and over == 0:
        true_or_false = 0
        print(guess_word)

        print("Letters used: ", directory)               # Shows letters which have been used to avoid repeating letters
        letter = input("Input letter: ")
        letter = letter.upper()                                                         # To avoid case sensitive errors
        directory.append(letter)                                      # Appends letters to the directory of used letters

        for i in range(len(word)):

            if letter == word[i]:                                                          # Checks if letter is in word
                guess_word[i] = letter
                print(guess_word)
                true_or_false = 1

        if true_or_false == 0:
            trial += 1

        print()

        if trial == 0:
            print("_____")
            print("    |")
            print("")
            print("")
            print("")
            print("")
            print("\n6 tries left\n")

        if trial == 1:
            print("_____")
            print("    |")
            print("    O")
            print("")
            print("")
            print("")
            print("\n5 tries left\n")

        if trial == 2:
            print("_____")
            print("    |")
            print("    O")
            print("    |")
            print("")
            print("")
            print("\n4 tries left\n")

        if trial == 3:
            print("_____")
            print("    |")
            print("    O")
            print("   /|")
            print("")
            print("")
            print("\n3 tries left\n")

        if trial == 4:
            print("_____")
            print("    |")
            print("    O")
            print("   /|\\")
            print("")
            print("\n2 tries left\n")

        if trial == 5:
            print("_____")
            print("    |")
            print("    O")
            print("   /|\\")
            print("   / ")
            print("\n1 try left\n")

        if trial == 6:
            print("_____")
            print("    |")
            print("    O")
            print("   /|\\")
            print("   / \\")
            print("\nYOU FAILED!\n")
            time.sleep(3)

        word_guess_word = ''.join(guess_word)                                                  # Converts list to string

        if word == word_guess_word:                                         # Checks if word has been completely guessed
            over = 1

    if trial != 6:
        print("\n\n\n\n\n\n\n\nYOU WON!")
        print("The word was ", word_guess_word, ".", sep='')
        time.sleep(3)


# ----------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTION
choice = 0

while choice != 4:

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("1. Mad-libs          Output time: 10 seconds")
    print("2. Tic Tac Toe       Output time: 3 seconds")
    print("3. Hangman           Output time: 3 seconds")
    print("4. Exit")

    choice = int(input("\nWhich one would you like to choose [1, 2, 3, 4]: "))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if choice == 1:
        mad_libs()
    elif choice == 2:
        tic_tac_toe()
    elif choice == 3:
        hangman()
    elif choice == 4:
        break
    else:
        print("Error 404. Choice not found.")

# ----------------------------------------------------------------------------------------------------------------------
