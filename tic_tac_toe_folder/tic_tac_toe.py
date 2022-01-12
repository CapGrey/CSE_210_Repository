# 1. Name:
#      Jake Rammell
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe

import json

# The characters used in the Tic-Tac-Toe board.
X = 'X'
O = 'O'
BLANK = ' '

# This is to enhance readability, "X" will be blue, "O" will be red,
# and everything else will be green.
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[31m"

# A blank Tic-Tac-Toe board.
blank_board = [
                "1", "2", "3",
                "4", "5", "6",
                "7", "8", "9" ]
        

json_file = "tic_tac_toe.json"

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename) as board_json:
            board_dict = json.load(board_json)

        board = board_dict["board"]

    #Create a save file in one does not exist.
    except:
        board_dict = {"board": blank_board}
        with open(filename, "w") as save_file:
            json.dump(board_dict, save_file)

        board = board_dict["board"]    

    
    return board

def save_board(filename, board):
    '''Save the current game to a file.'''
    json_board = {"board": board}
    with open(filename, "w") as save_file:
        json.dump(json_board, save_file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    colors = []
    for tile in board:
        if tile == "X":
            token_color = BLUE

        elif tile == "O":
            token_color = RED

        else:
            token_color = GREEN
        
        colors.append(token_color)

    print(f" {colors[0]}{board[0]} {GREEN}| {colors[1]}{board[1]} {GREEN}| {colors[2]}{board[2]} ")
    print(f"{GREEN}---+---+---")
    print(f" {colors[3]}{board[3]} {GREEN}| {colors[4]}{board[4]} {GREEN}| {colors[5]}{board[5]} ")
    print(f"{GREEN}---+---+---")
    print(f" {colors[6]}{board[6]} {GREEN}| {colors[7]}{board[7]} {GREEN}| {colors[8]}{board[8]} {GREEN}")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_count = 0
    o_count = 0
    for element in board:
        if element == "X":
            x_count += 1
        
        elif element == "O":
            o_count += 1

    if x_count > o_count:
        return False

    else:
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''

    # Determine who's turn it is.
    x_turn = is_x_turn(board)

    if x_turn:
        token = X
        user_position = input("X> ") 

    else:
        token = O
        user_position = input("O> ")

    # Confirm user input is valid.
    if user_position.lower() == "q":
         return True

    else:
        try:
            index_position = int(user_position) - 1

        # Confirm the space is available.
            if board[index_position] != "X" and board[index_position] != "O":
                board[index_position] = token


            else:
                print("that position is already filled")
        
        except:
            print("invalid input")
            print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")

def game_done(board):
    '''Determine if the game is finished.
    '''

    game_end = False
    # Game is finished if someone has completed a row.
    win = False

    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            print("The game was won by", board[row * 3])
            game_end = True
            win = True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col] and win == False:
            print("The game was won by", board[col])
            game_end = True
            win = True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]) and win == False:
        print("The game was won by", board[4])
        game_end = True
        win = True

    # Game is finished if all the squares are filled.
    if not win:
        tie = True
        for square in board:
            if square != "X" and square != "O":
                tie = False
        if tie:
            print("The game is a tie!")
            game_end = True

    if game_end:
        return True

    else:
        return False



def main():
    # display the instructions to the user.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")
    # retrieve the board.
    game_finished = False
    board = read_board(json_file)
    
    while not game_finished:
        display_board(board)
        print()
        user_quit = play_game(board)

        # Save and quit if user quits.
        if user_quit:
            game_finished = True
        
        # Check if the game is over.
        else:
            game_quit = game_done(board)
            if game_quit:
                display_board(board)
                board = blank_board
                game_finished = True

        save_board(json_file, board)



if __name__ == "__main__":
    main()