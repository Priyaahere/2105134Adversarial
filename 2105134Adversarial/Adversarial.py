import sys

def minimax(board, depth, maximizing_player):
    # Check if the game is over
    if is_terminal_state(board):
        return utility(board)

    # Initialize variables for the minimax search
    best_value = -float('inf') if maximizing_player else float('inf')
    best_move = None

    # Generate all possible moves for the current player
    for i, block in enumerate(board):
        if block == '0':
            new_board = list(board)
            new_board[i] = 'W' if maximizing_player else 'B'

            # Apply the flip rule if necessary
            flip_blocks(new_board, i)

            # Recursively calculate the minimax value for the new board
            value = minimax(new_board, depth - 1, not maximizing_player)

            # Update the best value and move if necessary
            if maximizing_player:
                if value > best_value:
                    best_value = value
                    best_move = i
            else:
                if value < best_value:
                    best_value = value
                    best_move = i

    return best_value, best_move

def is_terminal_state(board):
    # Check if there are any empty blocks left
    for block in board:
        if block == '0':
            return False

    return True

def utility(board):
    # Count the number of black and white coins
    black_coins = 0
    white_coins = 0

    for block in board:
        if block == 'B':
            black_coins += 1
        elif block == 'W':
            white_coins += 1

    # Return the utility for Player 1 (Player MAX)
    return black_coins if maximizing_player else white_coins

def flip_blocks(board, index):
    # Check for blocks to the left
    if index > 0 and board[index - 1] != '0':
        for i in range(index - 1, 0, -1):
            if board[i] == '0':
                break
            if board[i] == 'B':
                board[i] = 'W'
            elif board[i] == 'W':
                board[i] = 'B'
            else:
                break

    # Check for blocks to the right
    if index < len(board) - 1 and board[index + 1] != '0':
        for i in range(index + 1, len(board)):
            if board[i] == '0':
                break
            if board[i] == 'B':
                board[i] = 'W'
            elif board[i] == 'W':
                board[i] = 'B'
            else:
                break

# Get input from the user
board = input("Enter the board state: ")

# Determine the depth of the minimax search
depth = int(input("Enter the depth of the search: "))

# Determine the maximizing player
maximizing_player = bool(input("Is Player 1 the maximizing player (True/False): "))

# Calculate the minimax value and best move
value, move = minimax(board, depth, maximizing_player)

# Print the results
print("Best value:", value)
print("Best move:", move)