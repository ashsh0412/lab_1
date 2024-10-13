def initialize_board(num_rows, num_cols):
    return [["-" for _ in range(num_cols)] for _ in range(num_rows)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def insert_chip(board, col, chip_type):
    for row in reversed(range(len(board))):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row
    return -1  # Column is full

def check_if_winner(board, col, row, chip_type):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        for i in range(1, 4):
            r, c = row + i*dy, col + i*dx
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == chip_type:
                count += 1
            else:
                break
        
        for i in range(1, 4):
            r, c = row - i*dy, col - i*dx
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == chip_type:
                count += 1
            else:
                break
        
        if count >= 4:
            return True
    
    return False

def is_board_full(board):
    return all(cell != "-" for row in board for cell in row)

def play_game():
    while True:
        try:
            num_rows = int(input("What would you like the height of the board to be? "))
            num_cols = int(input("What would you like the length of the board to be? "))
            if num_rows < 4 or num_cols < 4:
                print("The board must be at least 4x4.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers.")

    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print("\nPlayer 1: x\nPlayer 2: o\n")

    players = ["x", "o"]
    current_player = 0

    while True:
        player = players[current_player]
        while True:
            try:
                if current_player == 0:
                    col = int(input("\nPlayer 1: Which column would you like to choose?\n"))
                else:
                    col = int(input("Player 2: Which column would you like to choose?\n"))
                
                if 0 <= col < num_cols:
                    row = insert_chip(board, col, player)
                    if row != -1:
                        break
                    else:
                        print("Column is full. Try another column.")
                else:
                    print(f"Invalid column. Please choose a column between 0 and {num_cols - 1}")
            except ValueError:
                print("Please enter a valid column number.")

        print_board(board)

        if check_if_winner(board, col, row, player):
            print(f"Player {current_player + 1} won the game!")
            break

        if is_board_full(board):
            print("Draw. Nobody wins.")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_game()