# ITP Project — Python Board Game

Introduction to Programming (ITP) group project implementing a terminal-based, two-player connect-in-a-row game. The engine supports human input and dynamically loaded Python player strategies.

## Requirements

- Python 3 (verified with Python 3.14.3).
- VS Code with your Python interpreter configured.
- Git for cloning and syncing the repository.

The repository is public; no GitHub account is required to clone or download it. Push access requires collaborator permissions.

The project uses only the Python standard library. No external dependencies or API keys are required; a virtual environment is optional.

## Clone and run

From a terminal in your preferred projects directory:

```powershell
git clone https://github.com/zentverse/itp-project.git
cd itp-project
code .
```

If `code` is unavailable, open the cloned folder using **File > Open Folder** in VS Code. Without Git, use **Code > Download ZIP** on GitHub, extract the archive, and open the folder containing `game.py`.

Run from the repository root in VS Code's integrated terminal:

```powershell
python -X utf8 game.py
```

On Windows, `py -X utf8 game.py` is an alternative if you use the Python launcher. The UTF-8 flag avoids encoding errors when printing the board symbols. Run in a terminal that accepts interactive input.

The working directory must contain `game.py` and the `player_*.py` modules: player discovery uses the current directory.

## Game configuration

The CLI prompts for two player names, a move timeout, and a round count:

| Prompt | Example | Meaning |
| --- | --- | --- |
| `Select player 1 (o):` | `ai` | Strategy controlling player 1. |
| `Select player 2 (x):` | `random` | Strategy controlling player 2. |
| `Enter the move timeout in seconds (0 for no timeout):` | `0` | Disable the turn time limit. |
| `Enter the number of rounds:` | `3` | Play three rounds and print results. |

Available players:

| Name | Implementation |
| --- | --- |
| `human` | Reads a column number from standard input. Displayed column numbers are one-based. |
| `random` | Chooses uniformly from the available columns. |
| `ai` | Tries the zero-based sequence `[2, 2, 1, 3, 0]`, skipping unavailable moves, then falls back to random selection. Prints board, choices, and memory for debugging. |

Use `human` for both players to play locally against another person. Use timeout `0` for interactive play. Press **Ctrl+C** to stop.

### Current engine behavior

- Each round randomly selects a square board size from 3 to 10, a winning line length from 3 to the board size, and the starting player.
- Pieces stack from the bottom of the selected column. Horizontal, vertical, and diagonal lines can win.
- The CLI currently does not display the winning line length.
- If the board fills without a line winner, the lower average move time determines the winner; equal averages favor player 1.
- A player exception, illegal move, or exceeded timeout awards the round to the opponent. Timeout is checked after the callback returns; it does not interrupt execution.
- An equal number of round wins favors player 1 in the overall result.

## Project structure

```text
itp-project/
├── game.py           # Game engine, player discovery, interactive CLI
├── player_ai.py      # Team strategy under development
├── player_human.py   # Interactive player
├── player_random.py  # Random baseline
├── .gitignore        # Python caches, local environments, editor files, secrets
└── README.md
```

## Developing a player

Edit `player_ai.py` to change the team strategy. To add another strategy, create `player_<name>.py` in the repository root and export a `play` function. The engine discovers the module at startup and lists it as `<name>`.

The callback contract is:

```python
from typing import Any, List, Tuple


def play(
    board: List[List[int]],
    choices: List[int],
    player: int,
    memory: Any,
) -> Tuple[int, Any]:
    move = choices[0]
    return move, memory
```

| Argument / return value | Contract |
| --- | --- |
| `board` | List of columns; each column contains occupied cells from bottom to top. Cell values are player IDs `0` and `1`. |
| `choices` | Zero-based indices of non-full columns. Return one of these indices. |
| `player` | Current player ID: `0` for `o`, `1` for `x`. |
| `memory` | State returned by this player on its previous turn; initially `None` for each round. |
| Return value | `(move, updated_memory)`, where `move` is a valid column index. |

The engine passes deep copies of `board` and `choices`, so changing them does not change the live board. Use the returned memory value to persist state between turns. The callback is not given the board height or winning line length; account for that limitation when designing a strategy.

The current `ai` player is a scripted strategy, not a trained machine-learning model.

## Verification

Check that all modules compile:

```powershell
python -m py_compile game.py player_ai.py player_human.py player_random.py
```

Run a three-round smoke test without human moves (PowerShell):

```powershell
@('ai', 'random', '0', '3') | python -X utf8 game.py
```

Expected: all three players are discovered, three rounds finish, and a summary is printed. Board sizes, moves, winners, and timing vary between runs. This is a smoke test, not a comprehensive test suite.

For interactive changes, also run `python -X utf8 game.py` with `human` and `random` and enter valid column numbers.

## Syncing changes

Before starting work, update your local checkout:

```powershell
git pull --ff-only
```

Commit or stash local edits first if they block the update. After editing, review the diff and stage only the files you intend to publish. For example, after changing the team strategy:

```powershell
git diff
git add player_ai.py
git commit -m "Improve player strategy"
git push
```

Keep this README aligned with any changes to setup, the player interface, or game behavior.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Clone fails or GitHub returns 404 | Check the repository URL and your network connection. Public read access does not require authentication. |
| `game.py` cannot be found or no players are listed | Run from the repository root, with all player modules present. |
| A player module fails to load | Read the startup error; confirm the module imports successfully and exports `play`. |
| Player selection is rejected | Enter the exact lowercase name shown at startup, such as `ai`, `human`, or `random`. |
| Board output raises `UnicodeEncodeError` | Run with `-X utf8` as shown above. |
| Human player loses after input | Enter an available column number and disable the timeout for human play. Invalid input can end the round. |
| VS Code uses an unexpected Python version | Check the selected interpreter and run `python --version` in the terminal being used. |
