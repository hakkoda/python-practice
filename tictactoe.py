# Tic-Tac-Toe

# Do a cool tic-tac-toe title
# show who is X,O in the header
# keep track of the wins/loses

import random
from os import system

def draw_board(board):
    """Prints out the board parameter"""

    # "board" is a list of 10 strings representing the board (ignore index 0)
    system("clear")
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
    valid_options = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    while move not in valid_options or not is_space_free(board, move):
        print("What is your next move? (1-9)")
        move = int(input())

    return move

def choose_random_move_from_list(board, moves_list):
    """Returns a valid move from the passed list on the passed board, returns
    none if there is no valid move"""
    possible_moves = []

    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    """Given a board and the computer's letter, determine where to move and
    return that move"""
    player_letter = "X" if computer_letter == "O" else "O"

    # ==========================================================================
    # Tic-Tac-Toe AI:
    # ==========================================================================

    # 1) Check if we can win in the next move:
    for i in range(1, 10):
        board_copy = clone_board(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # 2) Check if player could win on their next move and block them.
    for i in range(1, 10):
        board_copy = clone_board(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # 3) Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1,3,7,9])
    if move != None:
        return move

    # 4) Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # 5) Move on one of the sides.
    return choose_random_move_from_list(board, [2,4,6,8])

def is_board_full(board):
    """Return True is every space on the board has been taken, otherwise return
    False"""
    for i in range(1,10):
        if is_space_free(board, i):
            return False

    return True

print("Welcome to Tic-Tac-Toe!") # TODO: make this fancy

while True:
    # Reset the board.
    the_board = [ " " ] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print(f"{turn} will go first")
    game_is_playing = True

    while game_is_playing:
        if turn == "player":
            # player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print("Hooray! You have won the game!")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            # computer's turn
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print("The computer has beaten you! You lose.")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break




# ==============================================================================
#                               BEGIN TEST CODE
# ==============================================================================

def test():
    # ==========================================================================
    # TEST THE choose_random_move_from_list FUNCTION
    # ==========================================================================

    for i in range(0, 10):
        #          0   1    2    3    4    5    6    7    8    9
        board = [ "", "X", "X", "X", "X", " ", " ", " ", " ", " " ]
        moves_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        random_move = choose_random_move_from_list(board, moves_list)
        print(f"random move is: {random_move}")
         
    # Test None moves scenario
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "X", "X", "X", "X", "X", "X", "X", "X", "X" ]
    moves_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    random_move = choose_random_move_from_list(board, moves_list)
    print(f"random move is: {random_move}")


    # ==========================================================================
    # TEST THE get_player_move FUNCTION
    # ==========================================================================

    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", " ", " ", " ", " ", " ", " ", " ", " ", " " ]
    move = get_player_move(board)
    print(f"move is: {move}")
    make_move(board, "X", move)
    draw_board(board)

    move = get_player_move(board)
    print(f"move is: {move}")
    make_move(board, "O", move)
    draw_board(board)

    move = get_player_move(board)
    print(f"move is: {move}")
    make_move(board, "X", move)
    draw_board(board)


    # ==========================================================================
    # TEST THE clone_board FUNCTION
    # ==========================================================================
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    clone = clone_board(board)
    print(board)
    print(clone)


    # ==========================================================================
    # TEST THE is_winner FUNCTION
    # ==========================================================================

    #               0   1    2    3    4    5    6    7    8    9
    top_winner = [ "", "1", "2", "3", "4", "5", "6", "X", "X", "X" ]
    result = is_winner(top_winner, "X")
    print(f"top winner: {result}")

    #                  0   1    2    3    4    5    6    7    8    9
    bottom_winner = [ "", "O", "O", "O", "4", "5", "6", "7", "8", "9" ]
    result = is_winner(bottom_winner, "O")
    print(f"bottom winner: {result}")


    # ==========================================================================
    # TEST THE make_move FUNCTION
    # ==========================================================================
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


    # ==========================================================================
    # TEST THE who_goes_first FUNCTION
    # ==========================================================================
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")
    first_player = who_goes_first()
    print(f"first player: {first_player}")


    # ==========================================================================
    # TEST THE input_player_letter FUNCTION
    # ==========================================================================
    x_first = input_player_letter()
    print(f"x first: {x_first}")

    o_first = input_player_letter()
    print(f"o first: {o_first}")


    # ==========================================================================
    # TEST THE draw_board FUNCTION
    # ==========================================================================

    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "O", "O", "O", "O", "O", "O", "O", "O", "O" ]
    draw_board(board)
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "X", "X", "X", "X", "X", "X", "X", "X", "X" ]
    draw_board(board)
    #          0   1    2    3    4    5    6    7    8    9
    board = [ "", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    draw_board(board)

#test()
