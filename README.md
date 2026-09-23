# ITP Project — Python Board Game

Group project for **Introduction to Programming (ITP)**. This is a two-player, connect-in-a-row game that runs in a text window on your computer. Pieces drop into columns, and players try to connect pieces horizontally, vertically, or diagonally.

You can play against another person, against a computer player, or watch two computer players compete. No extra Python packages, paid services, or API keys are needed.

## Set up on Windows — step by step

You only need to do these setup steps once. You do **not** need Git or a code editor for this method.

### 1. Install Python

Python is the program that runs this game.

1. Open [the official Python downloads page](https://www.python.org/downloads/).
2. Download and install Python 3 for Windows, following the installer instructions. If you see an **Add Python to PATH** checkbox, select it.
3. After installation, open the Windows Start menu, type **PowerShell**, and open it. PowerShell is a window where you type instructions for your computer.
4. Type the following, then press **Enter**:

   ```powershell
   python --version
   ```

5. You should see a version number such as `Python 3.14.3`. If that does not work, try `py --version`. When `py` works, use `py` instead of `python` in the commands below.

This project was tested with Python 3.14.3.

### 2. Download the project from GitHub

1. Open [the ITP project repository](https://github.com/zentverse/itp-project). If the repository is private, sign in to a GitHub account that has access.
2. Click the green **Code** button, then choose **Download ZIP**.
3. Find the downloaded ZIP file, usually in your **Downloads** folder.
4. Right-click the ZIP file and select **Extract All**, then **Extract**. This creates a normal folder that you can use.
5. Move the extracted folder to a convenient place, such as **Documents**.
6. Open the folders inside it until you can see `game.py`, `player_ai.py`, `player_human.py`, and `player_random.py` together. The project folder will usually be named `itp-project-main`.

Do not try to run the game from inside the ZIP file. Extract it first, and keep all four Python files in the same folder.

### 3. Open a command window in the project folder

1. In File Explorer, open the folder containing `game.py`.
2. Click the address bar at the top of File Explorer, where the folder location appears.
3. Type `powershell` and press **Enter**.

A PowerShell window opens in that folder. This matters because the game looks for its player files in the current folder.

### 4. Start the game

Type this in PowerShell and press **Enter**:

```powershell
python -X utf8 game.py
```

If you used `py --version` earlier, use this instead:

```powershell
py -X utf8 game.py
```

The `-X utf8` part helps Windows display the board symbols correctly. Leave the window open while playing. There is no separate app window or website.

## Play your first game

The game asks four questions. Type each answer and press **Enter**.

| Question shown by the game | Type this for your first game | What it means |
| --- | --- | --- |
| `Select player 1 (o):` | `human` | You control the `o` pieces. |
| `Select player 2 (x):` | `random` | The computer controls the `x` pieces. |
| `Enter the move timeout in seconds (0 for no timeout):` | `0` | You have unlimited time to choose a move. |
| `Enter the number of rounds:` | `1` | Play one round. |

When asked to select a column, type one of the numbers listed after `possible:` and press **Enter**. Your piece drops into that column. Use a listed number: invalid input can make you lose the round.

The starting player is chosen randomly. Each round also gets a random square board size from 3 to 10 and a random winning line length from 3 up to the board size. The current program does not display that required line length, but it checks for a winner automatically. If the board fills up without a line winner, the player with the faster average turn wins.

At the end, the game prints the winner and timing results. To play again, type `python -X utf8 game.py` (or `py -X utf8 game.py`) again. To stop at any time, press **Ctrl + C**; interruption text may appear, which is normal.

### Other ways to play

Enter these names exactly in lowercase when choosing players:

| Player name | What it does |
| --- | --- |
| `human` | A person chooses each column. Choose this for both players to share one computer. |
| `random` | The computer chooses a random available column. |
| `ai` | The team's current player: tries a fixed move sequence, skips unavailable moves, then chooses randomly. It also prints debugging information. |

For a quick demonstration without entering moves, choose `ai` and `random`, then `0` for the timeout and `1` for the number of rounds.

## Open the project again later

Your downloaded files stay on your computer. Open the folder containing `game.py`, type `powershell` in File Explorer's address bar, and run `python -X utf8 game.py` or `py -X utf8 game.py` again. You do not need to reinstall Python or download the project every time.

## Troubleshooting

| What you see | What to do |
| --- | --- |
| `python` is not recognized, or the Microsoft Store opens | Try `py -X utf8 game.py`. If `py` also fails, install Python from the official link above, then close and reopen PowerShell. |
| `can't open file ... game.py` | You opened PowerShell in the wrong folder. Repeat step 3 in the folder where `game.py` is visible. |
| No available players are listed | Make sure all four `.py` files are together and open PowerShell in that same folder. |
| `Input ... not allowed` when selecting a player | Enter exactly `human`, `random`, or `ai`, without quotation marks. |
| A player loses after entering a move | Enter only a column number listed as possible. Use a timeout of `0` when a person is playing. |
| Extra lines starting with `board===>`, `choices===>`, or `memory===>` | These are debugging messages from the current `ai` player. They are expected. |
| The board's symbols look wrong or a Unicode error appears | Try `python -X utf8 game.py` (or `py -X utf8 game.py`) in Windows Terminal. |
| GitHub shows a 404 page | Check the repository link and sign in with an account that has access to this private repository. |

## What the files do

| File | Purpose |
| --- | --- |
| `game.py` | Starts the game, displays the board, applies the rules, and prints results. |
| `player_human.py` | Lets a person enter moves. |
| `player_random.py` | Provides a computer player that chooses random moves. |
| `player_ai.py` | Contains the team's player strategy being developed. |
| `README.md` | This setup and usage guide. |

## Optional: download with Git

If you already have Git installed, open PowerShell in the folder where you want to keep the project and run these commands one at a time:

```powershell
git clone https://github.com/zentverse/itp-project.git
cd itp-project
python -X utf8 game.py
```

A private repository requires a GitHub account with access; complete Git's sign-in prompt if shown. Use `py -X utf8 game.py` if that is your working Python command.

To get later updates in a Git clone, open PowerShell in the project folder and run `git pull`. If Git reports local changes or a conflict, keep your work and resolve it before updating; do not delete your edits. With the ZIP method, download a fresh ZIP and extract it into a separate folder so you retain any changes made to your old copy.

## For contributors

Keep this README up to date whenever the setup, player names, or game behavior changes. The project currently uses only Python's standard library, so no `pip install` command is needed. The `ai` player is a work in progress, not a trained machine-learning model.
