#------Global Variables-------
#Game board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if game is still going
game_still_going = True

#who won? Or tie?
winner = None

#whos turn
current_player = "X"

#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a game of tic tac toe
def play_game():
    #Display initial game
    display_board()

    #While the game is still going
    while game_still_going:
        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()
    #The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#Handle a single turn of an arbitrary
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose position from 1-9: ")

    #For checking board aviabality
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_win()
    check_if_tie()

def check_for_win():
    #Set up global variables
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()

    #check diagnols
    diagonal_winner = check_diagnols()

    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    #Set up global variables
    global game_still_going
    # check if any the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
         # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_columns():
    #Set up global variables
    global game_still_going
    # check if any column have all the same value (and is nor empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
        # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return  board[1]
    elif column_3:
        return board[2]
    return
def check_diagnols():
    # Set up global variables
    global game_still_going
    # check if any column have all the same value (and is nor empty)
    diagnol_1 = board[0] == board[4] == board[8] != "-"
    diagnol_2 = board[6] == board[4] == board[2] != "-"

    # If any column does have match, flag that there is a win
    if diagnol_1 or diagnol_2:
        game_still_going = False
        # Return the winner (X or O)
    if diagnol_1:
        return board[0]
    elif diagnol_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #global variables we need
    global current_player
    #if current_player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
