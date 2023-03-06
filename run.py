import os
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


def play_sudoku(s):
    """
    Takes returned list of list from function and stores in variable board
    Checks the number entered by the user and calls a function
    which prints a sudoku board to the terminal.
    Gets the user to enter the row and column number
    Calls a function to change the board variable
    """


def main():
    """
    The main function for the sudoku program
    Runs all program functions
    """
    size = get_board_size()
    play_sudoku(size)


print("Welcome to Sudoku!\n")
main()
