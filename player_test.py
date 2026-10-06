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

    # ---------------------------------------------------------
    # 1. IMMEDIATE WIN
    # ---------------------------------------------------------
    #
    # Try every legal column.
    # If placing our piece there wins the game, play it.
    #

    for column in choices:

        board[column].append(player)

        if won(board, player, target):

            board[column].pop()

            return column, memory

        board[column].pop()

    # ---------------------------------------------------------
    # 2. IMMEDIATE BLOCK
    # ---------------------------------------------------------
    #
    # Check whether the opponent could win on their next move.
    #
    # For every legal column, temporarily place an opponent piece.
    # If that gives the opponent a winning line, we must play in
    # that column ourselves to block it.
    #

    opponent = 1 if player == 2 else 2

    for column in choices:

        board[column].append(opponent)

        if won(board, opponent, target):

            board[column].pop()

            # Play in the same column to block the opponent.
            return column, memory

        board[column].pop()

    # ---------------------------------------------------------
    # 3. CENTER CONTROL
    # ---------------------------------------------------------
    #
    # If there is no immediate win and no immediate threat,
    # prefer the column closest to the center.
    #

    center = len(board) // 2

    best_column = min(
        choices,
        key=lambda column: abs(column - center)
    )

    return best_column, memory


# Immediate winning move. +
# Immediate block. +
# Double threats (create two winning possibilities).
# Center control. +
# Evaluate open threats / potential winning lines, penalize opponent threats, and ignore blocked windows.+
# Minimax with alpha-beta pruning, but only search shallowly because the board can be as large as 10×10 and each move has a 1-second limit.
# Iterative deepening with a deadline.
# Move ordering: winning move > blocking move > double threat > center > strong potential > other.
# Gravity-aware reasoning: a move is a column append, so the AI must evaluate reachable positions rather than arbitrary cells.
# Use memory carefully; the target value is not passed directly to play().

# Be within the time limit of 1 second per move, and avoid exceeding it.
# If there are no  possible moves the player with the lowest time for turn wins, make our faster than the random. 