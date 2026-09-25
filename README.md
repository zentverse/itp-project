# ITP Project

Introduction to Programming group project.

## Setup

With Python, Git, and VS Code installed, run these commands in the folder where you want to keep the project:

```powershell
git clone https://github.com/zentverse/itp-project.git
cd itp-project
code .
```

If `code .` is unavailable, open the cloned folder through **File > Open Folder** in VS Code.

No additional Python packages are required.

## Run

Open the VS Code terminal in the project folder and run the convenience launcher:

```powershell
python run_game.py
```

On Windows, you can also use the Python launcher:

```powershell
py run_game.py
```

If you get a Unicode encoding error or the board symbols do not display correctly, try `python -X utf8 run_game.py` or `py -X utf8 run_game.py`.

Select `ai` and `random` for a preset run of three rounds with a one-second move timeout. For other player combinations, follow the prompts for timeout and round count. For a quick manual run, enter:

- Player 1: `ai`
- Player 2: `random`
- Move timeout: `0`
- Number of rounds: `1`

Choose `human` for either player to play yourself. Press **Ctrl+C** to stop.

## `game.py` and `run_game.py`

Both files start the same game but provide different command-line flows:

- **`game.py`** contains the core game implementation and its built-in command-line interface. It discovers `player_*.py` files, then asks you to choose players, set a move timeout, and enter the number of rounds. Each round uses a randomly selected board size and target length.
- **`run_game.py`** imports and uses the game code in `game.py`, and makes `ai.py` selectable as `ai`. When you choose `ai` versus `random`, it skips the timeout and round prompts and automatically plays three rounds with a one-second timeout per move. For other player combinations, it asks for the timeout and round count.


## Get updates

From the project folder:

```powershell
git pull --ff-only
```

## Progress so far

- We played around with the game to get familiar with how it works.
- We explored `game.py` and the other Python files to understand the game flow and how the players interact with it.
- We started building our AI player in `player_ai.py` and tested hardcoded moves.
- `player_wip.py` is a work-in-progress file for the exploratory work and implementation details behind our approach. It will contain the groundwork and source needed to understand what we are doing. Once the AI is finalized, that work will move into `ai.py`, which will replace `player_wip.py` as the final implementation.
- We experimented with `memory`, but we have not fully understood how to use it yet.

**Next session:** Start with `memory`—trace how it is passed into `play()` and returned between turns, then use it to track the AI's progress through the hardcoded moves.

## Proposed timeline

| Period (2026) | Group activities | Target |
| --- | --- | --- |
| September 23–27 | Understand `memory`, trace the hardcoded moves, and review `board`, `choices`, and `player`. Ask the lecturer how the winning target `m` should be handled and which opponents are used for assessment. | Everyone can explain the existing player and follow its state across turns. |
| September 28–October 4 | Simulate moves, develop win/block detection once `m` is clarified, and agree on a simple strategy. Test small examples. | A working first strategy that makes legal moves and handles the selected examples. |
| October 5–11 | Add limited look-ahead, measure execution time against the one-second limit, and test repeated games across board sizes. Use the October 8 project session for questions and try the university's upload checks. | A reliable player with recorded results and a clear list of remaining fixes. |
| October 12–16 | Fix problems, prepare the A4 landscape poster, rehearse the pitch of up to five minutes, and walk through the final code. | Aim to finish and submit by October 16, subject to the actual upload arrangements. Everyone should understand the submitted code. |
| October 17–19 | Keep time available for necessary corrections and a final rehearsal. | Confirm the submitted version and be ready to present. |
| October 20 | Project presentation, 10:00–11:45, according to the supplied timetable. | Present the project and answer questions. |

## Points from the support session

- Explain the AI's strategy on the poster.
- There is no need to show the code on the poster.
- The submission platform will automatically set the number of rounds and the move timeout; our AI does not need to choose them.
- The lecturer mentioned that the opponent will be a random player, which we understand to mean a player that makes random moves. However, we recall the assignment guidelines referring to a player developed last year. The exact opponent used for assessment remains unclear.

## Questions to confirm with the lecturer

None.

## Strategy

- Take the middle column. The middle column is included in the most four-in-a-row lines possible. 
- The one who controls the middle has the most paths of attack.
- Build double threats. The strongest move is to create two threats at once – two different places where you can get four in a row next time. The opponent can only block one.
- Block in time. Always keep an eye on your opponent's three-in-a-row and block before it's too late. Don't miss the diagonals.
- Think of "odd and even" rows. Advanced players count on which lines (counted from below) the threats end up on, as this determines who gets there first.
- Avoid building for the opponent. Each tile you place raises the column and can give your opponent a new seat on top – think one step ahead.

Common mistakes:

- To only focus on your own line and forget to watch the opponent.
- To miss the diagonal threats, which are the hardest to see.
- Filling in a column and thus giving the opponent a winning position directly above.
- Playing out to the edges too early instead of fighting for the middle.
