import os
import sys
import time


def get_board_size():
    """
    Get the required size board from the user as int
    """
    while True:
        print("You can play a 2x2 (easy) or 3x3 (hard) grid.")
        print("Enter either '2' for 2x2 or '3' for 3x3\n")
        squares = int(input("What size grid would you like?: "))
        print("Validating entry...\n")
        verified = verify_board_size(squares)

        if verified:
            print("Verified board size!")
            # Referenced from:
            # https://www.guru99.com/python-time-sleep-delay.html#3
            time.sleep(1.5)
            # Referenced from:
            # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    return squares


def verify_board_size(squares):
    """
    Takes user input as a parameter and checks if the number received
    is either '2' or '3'.
    Otherwise, raises an exception and prints to terminal.
    """
    try:
        if squares not in (2, 3):  # Used tuple as immutable
            raise ValueError(
                f"Only '2' or '3' accepted. You entered {squares}"
            )
    except ValueError as v_e:
        print(f"Invalid data: {v_e}, please try again.\n")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return False

    return True


def get_user_input(prompt, size, board):
    """
    Calls a function to check if the user enters 'quit'
    """
    while True:
        try:
            user_input = input(prompt)
            check_if_quit(user_input)
            check_if_submit(user_input, size, board)
            return user_input
        except ValueError as v_e:
            print(f"Invalid Entry: {v_e}, please try again.\n")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')


def play_sudoku(s):
    """
    Takes returned list of list from function and stores in variable board
    Checks the number entered by the user and calls a function
    which prints a sudoku board to the terminal.
    Gets the user to enter the row and column number
    Calls a function to change the board variable
    """
    board = sudoku_board(s)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if s == 2:
            print_2x2_board(board)
        else:
            print_3x3_board(board)
        print("Enter the number of the column or row you want to change")
        print("Enter 'submit' to check the final answer.")
        print("Enter 'quit' to quit the game at any time.\n")
        row = get_user_input("Enter the number of the row: ", s, board)
        col = get_user_input("Enter the number of the column: ", s, board)
        num = get_user_input("Enter the number to put in the cell: ", s, board)

        check_num = check_user_num(s, row, col, num)
        if check_num == "Wrong Number":
            continue

        amend_board(board, row, col, num)


def sudoku_board(size):
    """
    Stores list of list for sudoku game,
    depending on the size of the board
    """
    def_num = 0
    board_2 = [
        [def_num, 2, 4, def_num],
        [1, def_num, def_num, 3],
        [4, def_num, def_num, 2],
        [def_num, 1, 3, def_num]
    ]

    board_3 = [
        [def_num, def_num, def_num, def_num, 5, 6, def_num, def_num, def_num],
        [def_num, 6, 4, 2, def_num, def_num, def_num, def_num, def_num],
        [def_num, 8, def_num, 9, 1, 4, def_num, def_num, 6],
        [def_num, 3, 1, def_num, def_num, def_num, def_num, 2, def_num],
        [6, def_num, 8, def_num, def_num, def_num, 1, def_num, 3],
        [def_num, 5, def_num, def_num, def_num, def_num, 8, 6, def_num],
        [8, def_num, def_num, 6, 2, 9, def_num, 4, def_num],
        [def_num, def_num, def_num, def_num, def_num, 7, 2, 9, def_num],
        [def_num, def_num, def_num, 5, 8, def_num, def_num, def_num, def_num]
    ]

    if size == 2:
        return board_2
    else:
        return board_3


def print_2x2_board(board):
    """
    Iterates through a list of lists and prints the list
    in a 2x2 format
    """
    print("     1   2      3   4   ")
    print("  + ------- ++ ------- +")

    for i, row in enumerate(board):
        print(f"{i+1}", end=" ")
        print("|", end="")
        for num in row[:2]:
            print("{:3} ".format(num), end="")
        print(" ||", end="")
        for num in row[2:]:
            print("{:3} ".format(num), end="")
        print(" |")

        if i == 1:
            print("  + ------- ++ ------- +")

    print("  + ------- ++ ------- +\n")


def print_3x3_board(board):
    """
    Iterates through a list of lists and prints the list
    in a 3x3 format
    """
    print("     1   2   3      4   5   6      7   8   9   ")
    for i, row in enumerate(board):
        if i % 3 == 0:
            print("  + ----------- ++ ----------- ++ ----------- +")
        print(f"{i+1}", end=" ")
        print("|", end="")
        for num in row[:3]:
            print("{:3} ".format(num), end="")
        print(" ||", end="")
        for num in row[3:6]:
            print("{:3} ".format(num), end="")
        print(" ||", end="")
        for num in row[6:]:
            print("{:3} ".format(num), end="")
        print(" |")

    print("  + ----------- ++ ----------- ++ ----------- +\n")


def check_if_quit(var):
    """
    Checks if the user enters 'quit' to quit the game.
    """
    if var == "quit":
        print("\nThanks for playing!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()


def check_user_num(size, row, col, num):
    """
    Checks the size of the playing grid.
    Checks if the number entered by the user conforms
    to the numbers used in the grid
    If the number conforms, change the list variable to user number
    """
    r_num = int(row)
    c_num = int(col)
    u_num = int(num)
    if size == 2:
        try:
            if not (1 <= r_num <= 4 and 1 <= c_num <= 4 and 1 <= u_num <= 4):
                raise ValueError(
                    "Only numbers 1-4 accepted."
                )
        except ValueError as e:
            print(f"\nInvalid Entry: {e}, You entered {r_num, c_num, u_num}.")
            print("please try again.\n")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return "Wrong Number"
    else:
        try:
            if not (1 <= r_num <= 9 and 1 <= c_num <= 9 and 1 <= u_num <= 9):
                raise ValueError(
                    "Only numbers 1-9 accepted."
                )
        except ValueError as e:
            print(f"\nInvalid Entry: {e}, You entered {r_num, c_num, u_num}.")
            print("please try again.\n")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return "Wrong Number"


def amend_board(board, row, col, num):
    """
    Changes the board list values to user defined numbers
    """
    row = int(row) - 1
    col = int(col) - 1
    num = int(num)
    board[row][col] = num


def check_if_submit(var, size, final_board):
    """
    Checks if the user enters 'submit' to finish the game.
    """
    if var == "submit":
        correct_ans = correct_answer(size)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Checking your answer...")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        check_answer(final_board, correct_ans, size)


def correct_answer(size):
    """
    Stores the correct answers for each board.
    """
    # Puzzle referenced from https://github.com/Varshneyabhushan/kudoSudoku
    BOARD_2 = [
        [3, 2, 4, 1],
        [1, 4, 2, 3],
        [4, 3, 1, 2],
        [2, 1, 3, 4]
    ]

    # Puzzle from https://www.creativecenter.brother/en-gb
    BOARD_3 = [
        [1, 9, 7, 3, 5, 6, 4, 8, 2],
        [3, 6, 4, 2, 7, 8, 9, 1, 5],
        [2, 8, 5, 9, 1, 4, 3, 7, 6],
        [9, 3, 1, 8, 6, 5, 7, 2, 4],
        [6, 4, 8, 7, 9, 2, 1, 5, 3],
        [7, 5, 2, 1, 4, 3, 8, 6, 9],
        [8, 7, 3, 6, 2, 9, 5, 4, 1],
        [5, 1, 6, 4, 3, 7, 2, 9, 8],
        [4, 2, 9, 5, 8, 1, 6, 3, 7]
    ]

    if size == 2:
        return BOARD_2
    else:
        return BOARD_3


def check_answer(final_board, correct_ans, size):
    """
    Checks the final board against the correct answer.
    Calls a function depending on the result.
    """
    if final_board == correct_ans:
        congratulation_message()
        print("\nThanks for playing Sudoku!")
        time.sleep(2)
        sys.exit()
    else:
        incorrect_message()
        if size == 2:
            print_2x2_board(correct_ans)
            print("Heres what you submitted: ")
            print_2x2_board(final_board)
            print("\nThanks for playing Sudoku!")
            time.sleep(2)
            sys.exit()
        else:
            print_3x3_board(correct_ans)
            print("Heres what you submitted: \n")
            print_3x3_board(final_board)
            time.sleep(2)
            print("\nThanks for playing Sudoku!")
            time.sleep(2)
            sys.exit()


def congratulation_message():
    """
    Prints a congratulations message for solving the puzzle
    """
    print("Congratulations, you've solved sudoku!")
    time.sleep(1)
    # Code from:
    # https://emojicombos.com/party-popper-ascii-art
    print("⠀⠀⠀⠀⠀⠀⠠⢿⣿⠇⠀⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠸⠿⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠁⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣼⣯⣅⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⢀⣤⡀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⣠⠞⠋⣿⡇⢀⣽⠇⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠘⠛⠃⠀⢤⣤⣤⣿⣦⠀⠀⠀⠀⣰⣏⣀⡀⠘⠛⠛⠉⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⢀⣴⢾⣿⠉⠉⣿⠀⠀⠀⠐⣾⣷⠄⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⣾⠃⠀⠻⣶⠾⠋⠀⠀⠀⠈⠈⠁⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣶⣄⠀⠸⠏⠀⠀⠀⠀ ⠀⢀⡀⠀⠀⠀⠀⠀⢀⡀⠀")
    print("⠀⠀⠀⠀⠀⣦⠈⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣤⡀⢠⡿⠻⣦⣀⣠⣴⠾⠛⠁")
    print("⠀⠀⠀⠀⠸⣿⣷⣄⠻⣿⣿⣿⣿⣿⣷⡄⠀⠈⠻⠟⠁⠀⠈⠉⠁⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⣄⠙⠻⣿⣷⣌⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⢠⣶⡄⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠸⣿⣿⣦⣈⠙⠿⣷⣄⠙⠻⠿⣿⠇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⢠⣦⣈⠙⠿⣿⣷⣦⡄⠉⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⣼⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(1)


def incorrect_message():
    """
    Prints a condolence message for not solving the puzzle
    """
    print("I'm sorry, thats the wrong answer...\n")
    time.sleep(1)
    print("Here's the correct answer:\n")


def main():
    """
    The main function for the sudoku program
    Takes input from the user and responds accordingly
    Runs all program functions
    """
    size = get_board_size()
    play_sudoku(size)


print("Welcome to Sudoku!\n")
main()
