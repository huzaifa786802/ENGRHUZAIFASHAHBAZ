# TIC TAC TOE - Two Player Terminal Game
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    return all(cell != " " for row in board for cell in row)
def tic_tac_toe():
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("🎮 Welcome to Tic Tac Toe!")
    print("Player X goes first.\n")
    print_board(board)
    # Main game loop
    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numbers between 0 and 2.")
            continue
        # Check if move is valid
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)
                # Check win condition
                if check_winner(board, current_player):
                    print(f"🏆 Player {current_player} wins! Congratulations!")
                    break
                # Check draw condition
                elif is_draw(board):
                    print("🤝 It's a draw!")
                    break
                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("🚫 That cell is already taken. Try again.")
        else:
            print("⚠️ Row and column must be between 0 and 2. Try again.")
if __name__ == "__main__":
    tic_tac_toe()