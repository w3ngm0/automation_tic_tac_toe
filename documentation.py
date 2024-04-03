'''
A Tic-Tac-Toe game where two players take turns marking spaces on a 3x3 grid board, where one player wins
by getting three matches in either a row , column or the board is full resulting in a draw.

This program allows players to input their moves by specifying the row
and column. It checks for a win condition after each move and ends the game when a player wins or when the
board is full. The game is played in the console/terminal.

To play the game, run the 'main()' function.

Functions:
- 'print_board()': Prints the layout of the board.
- 'is_win(player)': Checks if the specified player has won the game.
- 'tally_wins(results)': Counts the number of wins during the game.
- 'main()': Main function to start the game and also handles player turns.

Parameters:
    - 'player': The current players are 'X' or 'O'
    - 'row': The row number where the player wants to place their mark.
    - 'col': The column number where the player wants to place their mark.
    - 'board': The 3x3 grid representing tic_tac_bug_toe board.
    - 'result': A list to store the result of each game round (win or lose).

Usage Example:
--------------
To play game run 'main()' function.

Additional Information:
-----------------------
- The game provides feedback on the current state of the board, the winner(if any), and the number of wins during the game.
- Players can play multiple rounds of the game by restarting the 'main()'.
'''