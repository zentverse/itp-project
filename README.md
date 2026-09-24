# ITP Project d

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

Open the VS Code terminal in the project folder and run:

```powershell
python game.py
```

On Windows, you can also use the Python launcher:

```powershell
py game.py
```

If you get a Unicode encoding error or the board symbols do not display correctly, try `python -X utf8 game.py` or `py -X utf8 game.py`.

Follow the prompts. For a quick run, enter:

- Player 1: `ai`
- Player 2: `random`
- Move timeout: `0`
- Number of rounds: `1`

Choose `human` for either player to play yourself. Press **Ctrl+C** to stop.

## Get updates

From the project folder:

```powershell
git pull --ff-only
```

## Progress so far

- We played around with the game to get familiar with how it works.
- We explored `game.py` and the other Python files to understand the game flow and how the players interact with it.
- We started building our AI player in `player_ai.py` and tested hardcoded moves.
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

## Questions to confirm with the lecturer

1. Should the AI choose the number of rounds and the move timeout, or should these be configured manually?
2. Will the opponent be the provided `random` player, or another player implementation that we do not yet have access to?

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