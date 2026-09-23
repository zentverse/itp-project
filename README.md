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
python -X utf8 game.py
```

On Windows, use `py -X utf8 game.py` if your Python command is `py`. The UTF-8 flag helps display the board symbols correctly.

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
