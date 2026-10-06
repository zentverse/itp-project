import random
from typing import Any, List, Tuple


def won(board, player, target):
    """Check if a player has a winning line."""

    cols = len(board)

    for x in range(cols):
        for y in range(len(board[x])):

            if board[x][y] != player:
                continue

            directions = [
                (1, 0),   # horizontal
                (0, 1),   # vertical
                (1, 1),   # diagonal
                (1, -1)   # other diagonal
            ]

            for dx, dy in directions:

                count = 1

                xx = x + dx
                yy = y + dy

                while (
                    0 <= xx < cols
                    and 0 <= yy < len(board[xx])
                    and board[xx][yy] == player
                ):
                    count += 1
                    xx += dx
                    yy += dy

                if count >= target:
                    return True

    return False


def play(
    board: List[List[int]],
    choices: List[int],
    player: int,
    memory: Any
) -> Tuple[int, Any]:

    # Target = 3 for now
    target = 3

    # Strategy 1: Imitate win, (explain)
    # Look for an immediate winning move.
    for column in choices:

        # Pretend to play in this column
        board[column].append(player)

        # Check if we win
        if won(board, player, target):

            # Undo the test move
            board[column].pop()

            # Actually choose this column
            return column, memory

        # Undo the test move
        board[column].pop()

    # If we cannot win immediately,
    # choose a random legal move for now.
    
    # Center control.
    center = len(board) // 2

    return min(choices, key=lambda column: abs(column - center)), memory





# Immediate winning move. +
# Immediate block. +
# Double threats (create two winning possibilities).
# Center control. +
# Evaluate open threats / potential winning lines, penalize opponent threats, and ignore blocked windows.
# Minimax with alpha-beta pruning, but only search shallowly because the board can be as large as 10×10 and each move has a 1-second limit.
# Iterative deepening with a deadline.
# Move ordering: winning move > blocking move > double threat > center > strong potential > other.
# Gravity-aware reasoning: a move is a column append, so the AI must evaluate reachable positions rather than arbitrary cells.
# Use memory carefully; the target value is not passed directly to play().

# Be within the time limit of 1 second per move, and avoid exceeding it.
# If there are no  possible moves the player with the lowest time for turn wins, make our faster than the random. 