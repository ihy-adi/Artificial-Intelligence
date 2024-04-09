def check_board(board):
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in winning_conditions:
        if board[condition[0]] != 0 and board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]]
    if 0 not in board:  # Board is full, it's a draw
        return 0
    return None


def print_board(board):
    print("Current State of the Board:\n")
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if board[index] == 0:
                print("- ", end=" ")
            elif board[index] == 1:
                print("O ", end=" ")
            elif board[index] == -1:
                print("X ", end=" ")
        print()
    print()


def minimax(board, player):
    result = check_board(board)
    if result is not None:
        return result * player

    best_score = -2
    best_move = None

    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, -player)
            board[i] = 0  # Undo move

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is None:
        return 0

    return best_score


def computer_turn(board):
    best_score = -2
    best_move = None

    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0  # Undo move

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 1


def user_turn(board):
    while True:
        try:
            p = int(input("Choose a location (1-9): "))
            if 1 <= p <= 9:
                if board[p - 1] == 0:
                    board[p - 1] = -1
                    break
                else:
                    print("Invalid move. That position is already taken.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Computer plays as X, and you play as O.")
    choice = input("Would you like to go first (1) or second (2)? ")
    choice = int(choice)

    board = [0] * 9

    for i in range(9):
        if check_board(board) is not None:
            break
        if (i + choice) % 2 == 0:
            computer_turn(board)
        else:
            print_board(board)
            user_turn(board)

    print_board(board)
    result = check_board(board)
    if result == 1:
        print("Computer wins!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()

#works
