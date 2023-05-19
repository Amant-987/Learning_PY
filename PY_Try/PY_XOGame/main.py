import os

board = [" "] * 9
player = "X"


def print_board():
    os.system("clear")
    print("  " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("------------")
    print("  " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("------------")
    print("  " + board[6] + " | " + board[7] + " | " + board[8] + " ")


def get_move():
    global player
    valid_move = False
    while not valid_move:
        move = input("Player " + player + ", enter your move (1-9): ")
        if (
            move.isdigit()
            and int(move) >= 1
            and int(move) <= 9
            and board[int(move) - 1] == " "
        ):
            valid_move = True
        else:
            print("Invalid move. Please try again.")
    board[int(move) - 1] = player
    if player == "X":
        player = "O"
    else:
        player = "X"


def check_win():
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    else:
        return False


def main():
    while not check_win() and " " in board:
        print_board()
        get_move()
    print_board()
    if check_win():
        print("Player " + player + " wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
