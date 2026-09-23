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

## Questions to confirm with the lecturer

1. Should the AI choose the number of rounds and the move timeout, or should these be configured manually?
2. Will the opponent be the provided `random` player, or another player implementation that we do not yet have access to?
