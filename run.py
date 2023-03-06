def get_board_size():
    """
    Get the required size board from the user as int
    """
    print("You can play a 2x2 (easy) or 3x3 (hard) grid.")
    print("Enter either '2' for 2x2 or '3' for 3x3\n")
    squares = int(input("What size grid would you like?: "))
    print("Validating entry...\n")
    verified = verify_board_size(squares)


def verify_board_size(squares):
    """
    Takes user input as a parameter and checks if the number received
    is either '2' or '3'.
    Otherwise, raises an exception and prints to terminal.
    """


def main():
    """
    The main function for the sudoku program
    Runs all program functions
    """
    get_board_size()


print("Welcome to Sudoku!\n")
main()