# Adversarial Search (2105134)
# Minimax Algorithm for Game

This program implements the minimax algorithm to determine the optimal strategy for Player 1 in a two-player game. The game consists of a board of length N, where each block can contain a black coin, a white coin, or be empty. Players take turns placing their coins on empty blocks, and whenever a coin is placed adjacent to other coins of the same color, those coins flip to the opposite color. The game ends when there are no more empty blocks, and the player with the most coins of their color wins.

To run the program, follow these steps:

1. Save the code as `adversarial.py`.
2. Open a terminal window and navigate to the directory where you saved the code.
3. Run the following command:

```bash
python adversarial.py


4. The program will prompt you to enter the board state and the depth of the minimax search.
5. Enter the board state as a string of characters, where '0' represents an empty block, 'B' represents a black coin, and 'W' represents a white coin.
6. Enter the depth of the minimax search as an integer.
7. The program will then calculate the minimax value and best move for the given game state and print the results to the console.

## Example Usage


Enter the board state: 0000W00BBW0
Enter the depth of the search: 3
Enter Is Player 1 the maximizing player (True/False): True
Best value: 3
Best move: 1


In this example, the board state is "0000W00BBW0", the depth of the search is 3, and Player 1 is the maximizing player. The program calculates that the best value for Player 1 is 3 (meaning that Player 1 can guarantee at least 3 black coins in the terminal state) and the best move is to place a black coin on the second block.

## Explanation of the Code

The code is divided into several functions:

- `minimax(board, depth, maximizing_player)`: This function implements the minimax algorithm. It recursively evaluates the minimax value of the given game state for the specified depth and maximizing player.

- `is_terminal_state(board)`: This function checks if the game is in a terminal state.

- `utility(board)`: This function calculates the utility of the given game state for the maximizing player.

- `flip_blocks(board, index)`: This function applies the flip rule when a coin is placed on a block.

The main part of the code prompts the user to enter the board state and the depth of the minimax search, determines the maximizing player, and calculates the minimax value and best move for the given game state. Finally, it prints the results to the console.
