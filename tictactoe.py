# Go to line 96 and fill in the test code

# Tic-Tac-Toe

import random

def draw_board(board):
    """Prints out the board parameter"""

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print()
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print()

def input_player_letter():
    """Let the player type which letter they want to be, returns a list with the
    player's letter as the first item and the computer's letter as the second"""
    letter = ""
    while not(letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()

    # The first element in the list is the player's letter; the second is the
    # computer's letter.
    if letter == "X":
        return [ "X", "O" ]
    else:
        return [ "O", "X" ]

def who_goes_first():
    """Randomly choose which player goes first"""
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    """Take a board and letter and determines if player is winner"""
    combinations = [
        [7,8,9], # top
        [4,5,6], # middle
        [1,2,3], # bottom
        [7,4,1], # down left side
        [8,5,2], # down middle
        [9,6,3], # down right side
        [7,5,3], # diagonal
        [9,5,1]  # diagonal
    ]

    result = False
    for combo in combinations:
        result = board[combo[0]] == letter and \
                 board[combo[1]] == letter and \
                 board[combo[2]] == letter
        if result:
            return True

    return False

def clone_board(board):
    clone = []

    for i in board:
        clone.append(i)

    return clone

def is_space_free(board, move):
    """Return True is the move is available on the board"""
    return board[move] == " "

def get_player_move(board):
    """Get player's moveo on the board"""
    move = 0
    valid_options = "1 2 3 4 5 6 7 8 9".split()
    while move not in valid_options or not is_space_free(board, move):
        print("What is your next move? (1-9)")
        move = int(input())

    return move


def test():
    # **************************************************************************
    # TEST THE get_player_move FUNCTION
    # **************************************************************************


    # TODO: write some test code for the get_player_move function...



    # **************************************************************************
    # TEST THE clone_board FUNCTION
    # **************************************************************************
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    clone = clone_board(board)
    print(board)
    print(clone)


    # **************************************************************************
    # TEST THE is_winner FUNCTION
    # **************************************************************************

    #               0   1    2    3    4    5    6    7    8    9
    top_winner = [ "", "1", "2", "3", "4", "5", "6", "X", "X", "X" ]
    result = is_winner(top_winner, "X")
    print(f"top winner: {result}")

    #                  0   1    2    3    4    5    6    7    8    9
    bottom_winner = [ "", "O", "O", "O", "4", "5", "6", "7", "8", "9" ]
    result = is_winner(bottom_winner, "O")
    print(f"bottom winner: {result}")


    # **************************************************************************
    # TEST THE make_move FUNCTION
    # **************************************************************************
    #          0   1    2    3    4    5    6    7    8    9
    #board = [ "", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    #letter = "X"
    #move = 1
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 2
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 3
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 4
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 5
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 6
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 7
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 8
    #make_move(board, letter, move)
    #draw_board(board)
    #move = 9
    #make_move(board, letter, move)
    #draw_board(board)


    # **************************************************************************
    # TEST THE who_goes_first FUNCTION
    # **************************************************************************
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")


    # **************************************************************************
    # TEST THE input_player_letter FUNCTION
    # **************************************************************************
    x_first = input_player_letter()
    print(f"x first: {x_first}")

    o_first = input_player_letter()
    print(f"o first: {o_first}")


    # **************************************************************************
    # TEST THE draw_board FUNCTION
    # **************************************************************************

    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "O", "O", "O", "O", "O", "O", "O", "O", "O" ]
    draw_board(board)
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "X", "X", "X", "X", "X", "X", "X", "X", "X" ]
    draw_board(board)
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    draw_board(board)

test()
