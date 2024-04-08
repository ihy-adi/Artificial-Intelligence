# 0 1 2
# 3 4 5
# 6 7 8


# incomplete still
def minimax(board, player):
    temp = check_b(board)
    if temp != 0:
        return temp

    post = -1
    ind = -2

    for i in range(9):
        if board[i] == 0:
            exit()

    return post


# analyze the board
def check_b(board):
    w = [[1, 2, 3], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(9):
        if board[w[i][0]] != 0 and board[w[i][0]] == board[w[i][1]] and board[w[i][0]] == board[w[i][2]]:
            return board[w[i][2]]
    return 0


# computers turn
def comp_turn(board):
    value = minimax(board, -1)

    return 0


def print_board(board):
    print("Printing the current state: \n\n")
    for i in range(9):
        if (i > 0) and (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        if board[i] == 1:
            print("O ", end=" ")
        if board[i] == -1:
            print("X ", end=" ")
    print("\n\n")


def user_turn(board):
    p = input("Choose location from between 0 to 9: ")
    p = int(p)
    if board[p - 1] != 0:
        print("Invalid move.")
        user_turn(board)
    else:
        board[p - 1] = 1


# main game
def main():
    print("Computer is X, you are O")
    choice = input("Would you like to go first (1) or second (2)")
    choice = int(choice)

    board = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 9):
        if check_b(board) != 0:
            break;
        if (i + choice) % 2 == 0:
            comp_turn(board)
        else:
            print_board(board)
            user_turn(board)

    x = check_b(board)
    if x == 1:
        print_board(board)
        print("Player wins")
    elif x == -1:
        print_board(board)
        print("Computer wins")
    else:
        print_board(board)
        print("Draw")


# driver code
main()


