"""Search-based player for the supplied gravity-based Connect-m game."""

from typing import Any, List, Tuple
import math
import time


def _won(board, player, target):
    cols = len(board)
    rows = max((len(c) for c in board), default=0)
    # A line wins if it contains target same-player cells. Since pieces are
    # stacked, checking the four axes from occupied cells is inexpensive.
    for x in range(cols):
        for y, p in enumerate(board[x]):
            if p != player:
                continue
            for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
                px, py = x - dx, y - dy
                if 0 <= px < cols and 0 <= py < len(board[px]) and board[px][py] == player:
                    continue
                count, xx, yy = 0, x, y
                while 0 <= xx < cols and 0 <= yy < rows and yy < len(board[xx]) and board[xx][yy] == player:
                    count += 1
                    xx += dx
                    yy += dy
                    if count >= target:
                        return True
    return False


def _evaluate(board, me, target):
    """Score all target-length windows; blocked windows cannot contribute."""
    opp = 1 - me
    cols = len(board)
    rows = max(len(c) for c in board)
    score = 0
    weights = [0, 2, 12, 80, 600, 5000, 40000, 300000, 2000000, 12000000, 100000000]
    for x in range(cols):
        for y in range(rows):
            for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
                ex, ey = x + (target - 1) * dx, y + (target - 1) * dy
                if not (0 <= ex < cols and 0 <= ey < rows):
                    continue
                a = b = 0
                for k in range(target):
                    xx, yy = x + k * dx, y + k * dy
                    if yy < len(board[xx]):
                        p = board[xx][yy]
                        a += p == me
                        b += p == opp
                if not (a and b):
                    if a:
                        score += weights[min(a, 10)]
                    elif b:
                        score -= int(weights[min(b, 10)] * 1.12)
    # Favor central columns, which participate in more potential lines.
    center = (cols - 1) / 2
    score += sum((1 - abs(x - center) / (center + 1)) * (1 if p == me else -1)
                 for x, c in enumerate(board) for p in c)
    return score


def play(board: List[List[int]], choices: List[int], player: int, memory: Any) -> Tuple[int, Any]:
    """Choose a legal column with iterative-deepening alpha-beta search."""
    if not choices:
        raise ValueError("No legal moves")
    cols = len(board)
    rows = max(cols, max((len(c) for c in board), default=0))
    # The supplied game chooses a random target but does not pass it to play().
    # Keep a per-round target guess from memory when available; otherwise use
    # the conservative 3-in-a-row tactical target (the minimum game target).
    target = memory.get("target", 3) if isinstance(memory, dict) else 3
    target = max(3, min(target, rows, cols))
    center = (cols - 1) / 2
    ordered = sorted(choices, key=lambda c: (abs(c - center), c))
    deadline = time.perf_counter() + 0.72

    # Immediate wins and blocks for the minimum winning run are always useful.
    for c in ordered:
        board[c].append(player)
        win = _won(board, player, target)
        board[c].pop()
        if win:
            return c, memory
    for c in ordered:
        board[c].append(1 - player)
        threat = _won(board, 1 - player, target)
        board[c].pop()
        if threat:
            return c, memory

    best_move = ordered[0]
    nodes = 0

    def search(pos, side, depth, alpha, beta):
        nonlocal nodes
        nodes += 1
        if nodes & 127 == 0 and time.perf_counter() >= deadline:
            raise TimeoutError
        if _won(pos, 1 - side, target):
            return -900000 - depth
        if depth == 0 or all(len(c) >= rows for c in pos):
            return _evaluate(pos, player, target) * (1 if side == player else 1)
        moves = [c for c in range(cols) if len(pos[c]) < rows]
        moves.sort(key=lambda c: (abs(c - center), c))
        maximizing = side == player
        value = -math.inf if maximizing else math.inf
        for c in moves:
            pos[c].append(side)
            child = search(pos, 1 - side, depth - 1, alpha, beta)
            pos[c].pop()
            if maximizing:
                value = max(value, child)
                alpha = max(alpha, value)
            else:
                value = min(value, child)
                beta = min(beta, value)
            if beta <= alpha:
                break
        return value

    for depth in range(1, 7):
        current_move = best_move
        current_score = -math.inf
        try:
            for c in ordered:
                board[c].append(player)
                value = search(board, 1 - player, depth - 1, -math.inf, math.inf)
                board[c].pop()
                if value > current_score:
                    current_score, current_move = value, c
            best_move = current_move
        except TimeoutError:
            break
    return best_move, memory
