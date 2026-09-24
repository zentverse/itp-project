# game.py — Line-by-Line Explanation

The game engine: board state, display, turn handling, timing, winner detection, player discovery, and interactive setup.

Checked against the local source on September 24, 2026. Line numbers refer to this snapshot; update this guide when the source changes.

## Reading this guide

The board is a list of columns, each storing pieces from bottom to top. Player ID `0` means `o`; ID `1` means `x`. Code uses zero-based column indices, while displayed column numbers start at 1.

## Python notation

- Indentation groups statements into classes, functions, loops, and conditions. The source column below trims indentation for readability; inspect the linked source file to see the nesting.
- `def` defines a function; `class` defines a type of object; `self` refers to the current object.
- `=` assigns a value; `==` compares values; `is None` tests for the missing-state sentinel.
- `[]` creates a list or indexes a sequence; `{}` creates an empty dictionary; `(a, b)` is a tuple.
- `return move, memory` returns a two-item tuple and stops that function call.
- `for` iterates; `while` repeats while a condition is true; `break` exits the nearest loop.
- A comprehension such as `[i for i in choices]` builds a list by iterating.
- `#` starts a comment. Blank lines organize the file without performing an action.
- Triple quotes enclose multiline strings. A string as the first statement of a function is its docstring.
- Type hints such as `List[int]` describe intended values. They do not validate arguments automatically.

Every physical source line is listed below, including comments, multiline descriptions, and blank lines. Literal text is HTML-escaped only so Markdown displays it correctly.

## Line-by-line explanation

Source: [game.py](game.py). 320 lines.


### Imports and player type

| Line | Source | Explanation |
| --- | --- | --- |
| 1 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 2 | <code># Imports:                                                                                           #</code> | Comment labeling or describing the following code: Imports:                                                                                           #. Python ignores this line. |
| 3 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 4 | *blank* | Blank line for readability; no action is performed. |
| 5 | <code>import random</code> | Imports the standard-library random module. Its functions select random moves, board sizes, or a starting player. |
| 6 | <code>import time</code> | Imports timing functions used to measure how long a player takes. |
| 7 | <code>import copy</code> | Imports copying tools; deepcopy duplicates the board including its nested column lists. |
| 8 | *blank* | Blank line for readability; no action is performed. |
| 9 | *blank* | Blank line for readability; no action is performed. |
| 10 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 11 | <code># Typing:                                                                                            #</code> | Comment labeling or describing the following code: Typing:                                                                                            #. Python ignores this line. |
| 12 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 13 | *blank* | Blank line for readability; no action is performed. |
| 14 | <code>from typing import Any, List, Dict, Tuple, Callable</code> | Imports type hints: Any for unrestricted values, List for lists, Dict for mappings, Tuple for returned groups, and Callable for functions. |
| 15 | <code>player_callable = Callable[[List[List[int]], List[int], int, Any], Tuple[int, Any]]</code> | Defines a type alias for a player function: it receives a list of integer lists, a list of integers, a player integer, and any memory value; it returns an integer move and any updated memory. This describes the interface, not executable player logic. |
| 16 | *blank* | Blank line for readability; no action is performed. |
| 17 | *blank* | Blank line for readability; no action is performed. |
| 18 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 19 | <code># Game Class:                                                                                        #</code> | Comment labeling or describing the following code: Game Class:                                                                                        #. Python ignores this line. |
| 20 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 21 | *blank* | Blank line for readability; no action is performed. |

### Game construction

| Line | Source | Explanation |
| --- | --- | --- |
| 22 | <code>class TicTacToe:</code> | Defines the TicTacToe class: a template bundling the board state and the methods that operate on it. |
| 23 | <code>def __init__(self, n_rows:int=5, n_cols:int=5, n_target:int=5, timeout:float=0) -&gt; None:</code> | Defines the constructor, called when creating a game. self is that game instance. Defaults are 5 rows, 5 columns, a target of 5, and timeout 0. The -> None hint says the constructor returns no result value. |
| 24 | <code>&#x27;&#x27;&#x27;Create a new TicTacToe game for two players.</code> | Explanatory string describing this function; it does not itself perform the described action. |
| 25 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 26 | <code>Arguments:</code> | Introduces the parameter descriptions in the explanatory string. |
| 27 | <code>n_rows    (int): number of rows of the board</code> | Description of the board input: a list of columns containing player IDs from bottom to top. |
| 28 | <code>n_cols    (int): number of columns of the board</code> | Description of the board input: a list of columns containing player IDs from bottom to top. |
| 29 | <code>n_target  (int): number of adjacent pieces needed to win</code> | Documents the consecutive-piece count needed to win. |
| 30 | <code>timeout (float): time for each turn in seconds</code> | Documents the move duration limit, measured in seconds. |
| 31 | <code>&#x27;&#x27;&#x27;</code> | Closes the multiline explanatory string. |
| 32 | <code>self.columns     = [[] for _ in range(n_cols)]</code> | Creates a separate empty list for every column. range(n_cols) repeats the expression n_cols times; _ is an unused loop variable. These are distinct lists, so adding to one does not add to the others. |
| 33 | <code>self.max_rows    = n_rows</code> | Stores the maximum column height on this game instance. |
| 34 | <code>self.target      = n_target</code> | Stores the number of consecutive pieces needed to win (the target m). |
| 35 | <code>self.timeout     = timeout</code> | Stores the time limit in seconds; zero disables the timeout check. |
| 36 | *blank* | Blank line for readability; no action is performed. |

### Drawing the board

| Line | Source | Explanation |
| --- | --- | --- |
| 37 | <code>def __repr__(self) -&gt; str:</code> | Defines the textual representation of a game. print(self) uses this method because the class has no separate __str__ method. |
| 38 | <code>&#x27;&#x27;&#x27;Create some ascii-art representing the current state of the game.&#x27;&#x27;&#x27;</code> | Explanatory string describing this function; it does not itself perform the described action. |
| 39 | <code>board = []</code> | Starts a list of display strings. This local board is a picture being assembled, not the actual self.columns data. |
| 40 | *blank* | Blank line for readability; no action is performed. |
| 41 | <code># add bottom:</code> | Comment labeling or describing the following code: add bottom:. Python ignores this line. |
| 42 | <code>board.append(&#x27;└&#x27; + &#x27;─&#x27;.join([&#x27;─&#x27; for _ in self.columns]) + &#x27;┘&#x27;)</code> | Builds the bottom border using corner symbols and joined horizontal strokes, then appends it to the display list. |
| 43 | *blank* | Blank line for readability; no action is performed. |
| 44 | <code>for i in range(self.max_rows):</code> | Visits row indices from 0 up to max_rows - 1, starting at the bottom of the stored board. |
| 45 | <code># print current row:</code> | Comment labeling or describing the following code: print current row:. Python ignores this line. |
| 46 | <code>row = [(&#x27;o&#x27;,&#x27;x&#x27;)[col[i]] if len(col) &gt; i else &#x27; &#x27; for col in self.columns]</code> | For each column, checks whether row i is occupied. If so, the stored ID indexes the tuple: 0 becomes o and 1 becomes x. Otherwise it adds a space. The comprehension produces one display row. |
| 47 | *blank* | Blank line for readability; no action is performed. |
| 48 | <code># print next row:</code> | Comment labeling or describing the following code: print next row:. Python ignores this line. |
| 49 | <code>board.append(&#x27;│&#x27; + &#x27; &#x27;.join(row) + &#x27;│&#x27;)</code> | Joins the row symbols with spaces, surrounds them with vertical borders, and adds that row to the display list. |
| 50 | *blank* | Blank line for readability; no action is performed. |
| 51 | <code># add top:</code> | Comment labeling or describing the following code: add top:. Python ignores this line. |
| 52 | <code>board.append(&#x27; &#x27; + &#x27; &#x27;.join([&#x27;↓&#x27; for _ in self.columns]) + &#x27; &#x27;)</code> | Adds a display line containing one downward arrow per column. |
| 53 | <code>board.append(&#x27; &#x27; + &#x27; &#x27;.join([str(i+1) for i, col in enumerate(self.columns)]) + &#x27; &#x27;)</code> | Uses enumerate to obtain each column index, adds 1 for human-readable numbering, converts it to text, and joins the numbers into a heading. |
| 54 | *blank* | Blank line for readability; no action is performed. |
| 55 | <code># print whole board:</code> | Comment labeling or describing the following code: print whole board:. Python ignores this line. |
| 56 | <code>return &#x27;\n  &#x27; + &#x27;\n  &#x27;.join(board[::-1])</code> | Reverses the display list with [::-1], so the heading appears first and the bottom border last. Joins its lines with newline-plus-indentation and returns the complete string. |
| 57 | *blank* | Blank line for readability; no action is performed. |

### Playing one round

| Line | Source | Explanation |
| --- | --- | --- |
| 58 | <code>def start(self, player1:player_callable, player2:player_callable) -&gt; Tuple[int, List[float], List[float]]:</code> | Defines the method that plays one round using two supplied player functions. Its result is (winner ID, player 0 timing list, player 1 timing list). |
| 59 | <code>&#x27;&#x27;&#x27; Start a game for two players.</code> | Explanatory string describing this function; it does not itself perform the described action. |
| 60 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 61 | <code>Arguments:</code> | Introduces the parameter descriptions in the explanatory string. |
| 62 | <code>player1 (player_callable): a callback performing the actions of player 1.</code> | Documents a player argument: callbacks choose moves; integer player IDs identify which pieces belong to the current player. |
| 63 | <code>player2 (player_callable): a callback performing the actions of player 2.</code> | Documents a player argument: callbacks choose moves; integer player IDs identify which pieces belong to the current player. |
| 64 | <code>&#x27;&#x27;&#x27;</code> | Closes the multiline explanatory string. |
| 65 | *blank* | Blank line for readability; no action is performed. |
| 66 | <code># game variables:</code> | Comment labeling or describing the following code: game variables:. Python ignores this line. |
| 67 | <code>callbacks = (player1, player2)</code> | Stores the two functions in a tuple, indexed by player ID. Functions can be stored and called later just like other values. |
| 68 | <code>memory = [None, None]</code> | Creates two separate memory slots, initially None. Each player receives only its own slot. Calling start for a new round resets both slots. |
| 69 | <code>times  = [[], []]</code> | Creates two separate lists for recording the duration of each player's completed callbacks. |
| 70 | <code>player = random.randint(0,1)</code> | Chooses a random initial ID, 0 or 1 inclusive. The ID is flipped before the first move, so the other ID actually moves first; the starting player is still random. |
| 71 | <code>winner = -1</code> | Uses -1 as a sentinel meaning that no winner has been found. |
| 72 | *blank* | Blank line for readability; no action is performed. |
| 73 | <code># print gameplan:</code> | Comment labeling or describing the following code: print gameplan:. Python ignores this line. |
| 74 | <code>print(self)</code> | Prints the initial board through __repr__. |
| 75 | *blank* | Blank line for readability; no action is performed. |
| 76 | <code>while winner &lt; 0:</code> | Repeats turns while winner is negative. A win or an explicit break ends this loop. |
| 77 | <code># get all possible columns:</code> | Comment labeling or describing the following code: get all possible columns:. Python ignores this line. |
| 78 | <code>choices = [i for i, col in enumerate(self.columns) if len(col) &lt; self.max_rows]</code> | Enumerates all columns and keeps only indices whose column contains fewer than max_rows pieces. The resulting choices are zero-based legal moves. |
| 79 | <code>if len(choices) == 0:</code> | Checks whether no legal moves remain, meaning the board is full. |
| 80 | <code>print(f&#x27;\nGame Over. Fastest player wins!&#x27;)</code> | Reports that the full-board result will be decided by average move time. |
| 81 | <code>t0, t1 = [sum(t)/len(t) for t in times]</code> | Computes sum(t) / len(t) for each timing list and unpacks the two averages into t0 and t1. This assumes both lists contain a time. |
| 82 | <code>winner = int(t1 &lt; t0)</code> | If player 1's average t1 is smaller, the comparison is True and int(True) gives winner ID 1. Otherwise winner ID 0 wins, including an exact tie. |
| 83 | <code>break</code> | Exits the round loop after the full-board time decision. |
| 84 | *blank* | Blank line for readability; no action is performed. |
| 85 | <code># get next player:</code> | Comment labeling or describing the following code: get next player:. Python ignores this line. |
| 86 | <code>player = (player + 1) % 2</code> | Switches players: (0 + 1) % 2 is 1 and (1 + 1) % 2 is 0. % is the remainder operator. |
| 87 | <code>print(f&quot;\nPlayer {player + 1:d}&#x27;s turn ({(&#x27;o&#x27;,&#x27;x&#x27;)[player]}):&quot;)</code> | Prints the one-based player number and its symbol. An f-string evaluates expressions inside braces; :d formats an integer in decimal. |
| 88 | *blank* | Blank line for readability; no action is performed. |
| 89 | <code># get next column from player (with timeout):</code> | Comment labeling or describing the following code: get next column from player (with timeout):. Python ignores this line. |
| 90 | <code>t = time.time()</code> | Records the current wall-clock time before preparing arguments and calling the player. |
| 91 | *blank* | Blank line for readability; no action is performed. |
| 92 | <code>try: move, memory[player] = callbacks[player](copy.deepcopy(self.columns), copy.deepcopy(choices), player, memory[player])</code> | Calls the selected function with deep copies of the board and legal choices, its ID, and its saved memory. Unpacks the returned pair into move and that player's memory slot. The copies protect the live board from edits inside the callback. The target and maximum height are not passed. |
| 93 | <code>except Exception as e:</code> | Catches ordinary exceptions raised while copying, calling the player, or unpacking the result, storing the exception in e. It does not catch KeyboardInterrupt. |
| 94 | <code>print(f&#x27;\nExeption in player {player + 1:d} code: {e}&#x27;)</code> | Prints the player number and error text. Exeption is a spelling mistake in the displayed message. |
| 95 | <code>winner = (player + 1) % 2</code> | Awards the round to the other player after an exception. |
| 96 | <code>break</code> | Stops the round after the exception. |
| 97 | *blank* | Blank line for readability; no action is performed. |
| 98 | <code>t = time.time() - t</code> | Subtracts the start timestamp from the current timestamp to get elapsed seconds. This includes copying and debug output inside the callback, not just the strategy calculation. |
| 99 | <code>times[player].append(t)</code> | Appends the measured duration to this player's timing list. |
| 100 | *blank* | Blank line for readability; no action is performed. |
| 101 | <code>if self.timeout &gt; 0 and t &gt; self.timeout:</code> | Checks whether a positive timeout is enabled and the measured duration exceeds it. This happens after the function returns; it cannot interrupt a function that never returns. |
| 102 | <code>print(f&#x27;\nPlayer {player + 1:d}\&#x27;s move timed out.&#x27;)</code> | Prints a timeout message. The backslash before the apostrophe keeps it inside the single-quoted string. |
| 103 | <code>winner = (player + 1) % 2</code> | Awards the round to the other player after a timeout. |
| 104 | <code>break</code> | Stops the round after the timeout. |
| 105 | *blank* | Blank line for readability; no action is performed. |
| 106 | <code>if move not in choices:</code> | Checks whether the returned move is absent from the legal choices. |
| 107 | <code>print(f&#x27;\nImpossible move by player {player + 1:d}. Column {move + 1:d} is already full.&#x27;)</code> | Reports an illegal move using one-based numbering. The message says full even for an out-of-range column. A non-integer value can also cause an error in the arithmetic or :d formatting here. |
| 108 | <code>winner = (player + 1) % 2</code> | Awards the round to the other player after an illegal move. |
| 109 | <code>break</code> | Stops the round after the illegal move. |
| 110 | *blank* | Blank line for readability; no action is performed. |
| 111 | <code># take turn:</code> | Comment labeling or describing the following code: take turn:. Python ignores this line. |
| 112 | <code>self.columns[move].append(player)</code> | Adds the player ID to the end of the selected column. Since columns are stored bottom-to-top, the piece lands above existing pieces. |
| 113 | <code>print(self)</code> | Prints the board after the move. |
| 114 | *blank* | Blank line for readability; no action is performed. |
| 115 | <code># check for winner:</code> | Comment labeling or describing the following code: check for winner:. Python ignores this line. |
| 116 | <code>winner = self.check_win()</code> | Checks every direction for a winning line; stores 0 or 1 if found, or -1 if play should continue. |
| 117 | *blank* | Blank line for readability; no action is performed. |
| 118 | <code># return winning player:</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |
| 119 | <code>print(f&#x27;\nPlayer {winner + 1:d} won the round!&#x27;)</code> | Prints the winner of this round, converting its internal ID to player number 1 or 2. |
| 120 | <code>for i, t in enumerate(times):</code> | Iterates over the two timing lists with their player indices. |
| 121 | <code>if len(t) &gt; 0: print(f&#x27;  Average time per turn player {i + 1:d}: {sum(t)/len(t)*1000.:.2f} ms&#x27;)</code> | Only for a nonempty timing list, prints its mean in milliseconds: seconds multiplied by 1000, formatted with two decimal places using :.2f. |
| 122 | *blank* | Blank line for readability; no action is performed. |
| 123 | <code>return (winner,) + tuple(times)</code> | Builds a one-item tuple (winner,) and concatenates it with the tuple of timing lists, giving (winner, times_for_0, times_for_1). The comma makes the first expression a tuple. |
| 124 | *blank* | Blank line for readability; no action is performed. |

### Checking for a winner

| Line | Source | Explanation |
| --- | --- | --- |
| 125 | <code>def check_win(self) -&gt; int:</code> | Defines the winner-checking method, returning an integer ID or -1. |
| 126 | <code>&#x27;&#x27;&#x27;Check whether any of the players has `target` adjacent pieces on the board (any direction).&#x27;&#x27;&#x27;</code> | Description of the board input: a list of columns containing player IDs from bottom to top. |
| 127 | *blank* | Blank line for readability; no action is performed. |
| 128 | <code># helper function checking single cells:</code> | Comment labeling or describing the following code: helper function checking single cells:. Python ignores this line. |
| 129 | <code>def check_cell(i, j, last, count):</code> | Defines a local helper for one cell. i is the column, j the row, last the previous piece ID, and count the current run length. |
| 130 | <code>if j &gt;= len(self.columns[i]):</code> | Checks whether row j is above the occupied part of column i, so that cell is empty. |
| 131 | <code>last, count = -1, 0</code> | An empty cell breaks a sequence: reset the previous ID to -1 and run length to zero. |
| 132 | *blank* | Blank line for readability; no action is performed. |
| 133 | <code>elif self.columns[i][j] == last:</code> | Otherwise checks whether this occupied cell matches the previously seen player ID. |
| 134 | <code>count += 1</code> | Extends the current sequence by one. |
| 135 | *blank* | Blank line for readability; no action is performed. |
| 136 | <code>else: last, count = self.columns[i][j], 1</code> | For a different occupied player ID, starts a new sequence of length one and records that ID. |
| 137 | *blank* | Blank line for readability; no action is performed. |
| 138 | <code>return last, count, count &gt;= self.target</code> | Returns the latest ID, run length, and a Boolean saying whether the run has reached or exceeded the target. |
| 139 | *blank* | Blank line for readability; no action is performed. |
| 140 | *blank* | Blank line for readability; no action is performed. |
| 141 | <code># vertically:</code> | Comment labeling or describing the following code: vertically:. Python ignores this line. |
| 142 | <code>for i in range(len(self.columns)):</code> | Starts a vertical scan for each column. |
| 143 | <code>last, count = -1, 0</code> | Resets tracking before scanning this column. |
| 144 | *blank* | Blank line for readability; no action is performed. |
| 145 | <code>for j in range(self.max_rows):</code> | Visits every row in that column from bottom to top. |
| 146 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 147 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes the cell and replaces last/count with the updated state; win is the returned Boolean. |
| 148 | *blank* | Blank line for readability; no action is performed. |
| 149 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 150 | <code>if win: return last</code> | If a vertical winning run is found, immediately returns its player ID from check_win. |
| 151 | *blank* | Blank line for readability; no action is performed. |
| 152 | *blank* | Blank line for readability; no action is performed. |
| 153 | <code># horizontally:</code> | Comment labeling or describing the following code: horizontally:. Python ignores this line. |
| 154 | <code>for j in range(self.max_rows):</code> | Starts a horizontal scan at each row height. |
| 155 | <code>last, count = -1, 0</code> | Resets sequence tracking for this row. |
| 156 | *blank* | Blank line for readability; no action is performed. |
| 157 | <code>for i in range(len(self.columns)):</code> | Visits columns left-to-right along the current row. |
| 158 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 159 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes this cell using the same sequence-counting helper. |
| 160 | *blank* | Blank line for readability; no action is performed. |
| 161 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 162 | <code>if win: return last</code> | Returns the player ID if a horizontal winning run is found. |
| 163 | *blank* | Blank line for readability; no action is performed. |
| 164 | *blank* | Blank line for readability; no action is performed. |
| 165 | <code># diagonally (up):</code> | Comment labeling or describing the following code: diagonally (up):. Python ignores this line. |
| 166 | <code>for i in range(len(self.columns)):</code> | Starts an upward-right diagonal at every bottom-edge column. |
| 167 | <code>j, last, count = 0, -1, 0</code> | Sets the starting row to zero and clears sequence tracking. |
| 168 | *blank* | Blank line for readability; no action is performed. |
| 169 | <code>while i &lt; len(self.columns) and j &lt; self.max_rows:</code> | Continues while both column and row indices stay inside the board. |
| 170 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 171 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes the current diagonal cell and updates its run. |
| 172 | *blank* | Blank line for readability; no action is performed. |
| 173 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 174 | <code>if win: return last</code> | Returns the winner if this upward-right scan reaches the target. |
| 175 | *blank* | Blank line for readability; no action is performed. |
| 176 | <code>i += 1</code> | Moves one column to the right. |
| 177 | <code>j += 1</code> | Moves one row upward, completing the diagonal step. |
| 178 | *blank* | Blank line for readability; no action is performed. |
| 179 | <code>for j in range(self.max_rows):</code> | Starts another upward-right scan from each left-edge row; these cover diagonals not reached from the bottom edge. |
| 180 | <code>i, last, count = 0, -1, 0</code> | Sets the initial column to zero and resets tracking. |
| 181 | *blank* | Blank line for readability; no action is performed. |
| 182 | <code>while i &lt; len(self.columns) and j &lt; self.max_rows:</code> | Continues until the scan leaves the right or top edge. |
| 183 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 184 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes this diagonal cell. |
| 185 | *blank* | Blank line for readability; no action is performed. |
| 186 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 187 | <code>if win: return last</code> | Returns a winner if this scan reaches the target. |
| 188 | *blank* | Blank line for readability; no action is performed. |
| 189 | <code>i += 1</code> | Moves one column right. |
| 190 | <code>j += 1</code> | Moves one row up. |
| 191 | *blank* | Blank line for readability; no action is performed. |
| 192 | *blank* | Blank line for readability; no action is performed. |
| 193 | <code># diagonally (down):</code> | Comment labeling or describing the following code: diagonally (down):. Python ignores this line. |
| 194 | <code>for i in range(len(self.columns)):</code> | Starts a downward-right diagonal at each top-edge column. |
| 195 | <code>j, last, count = self.max_rows-1, -1, 0</code> | Sets the starting row to the top row and resets tracking. |
| 196 | *blank* | Blank line for readability; no action is performed. |
| 197 | <code>while i &lt; len(self.columns) and j &gt;= 0:</code> | Continues while the scan has not crossed the right or bottom edge. |
| 198 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 199 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes this diagonal cell. |
| 200 | *blank* | Blank line for readability; no action is performed. |
| 201 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 202 | <code>if win: return last</code> | Returns the winner if the target is reached on this diagonal. |
| 203 | *blank* | Blank line for readability; no action is performed. |
| 204 | <code>i += 1</code> | Moves one column right. |
| 205 | <code>j -= 1</code> | Moves one row down. |
| 206 | *blank* | Blank line for readability; no action is performed. |
| 207 | <code>for j in range(self.max_rows):</code> | Starts scans at each right-edge row, covering the remaining diagonals of this slope. |
| 208 | <code>i, last, count = len(self.columns)-1, -1, 0</code> | Starts at the last column and resets tracking. |
| 209 | *blank* | Blank line for readability; no action is performed. |
| 210 | <code>while i &gt;= 0 and j &lt; self.max_rows:</code> | Continues while the scan has not crossed the left or top edge. |
| 211 | <code># check cell:</code> | Comment labeling or describing the following code: check cell:. Python ignores this line. |
| 212 | <code>last, count, win = check_cell(i, j, last, count)</code> | Processes this diagonal cell. |
| 213 | *blank* | Blank line for readability; no action is performed. |
| 214 | <code># exit on win:</code> | Comment labeling or describing the following code: exit on win:. Python ignores this line. |
| 215 | <code>if win: return last</code> | Returns the winner if the target is reached. |
| 216 | *blank* | Blank line for readability; no action is performed. |
| 217 | <code>i -= 1</code> | Moves one column left. |
| 218 | <code>j += 1</code> | Moves one row up. This traverses the same slope as downward-right, but in the opposite direction. |
| 219 | *blank* | Blank line for readability; no action is performed. |
| 220 | <code>return -1</code> | Returns -1 after every scan has finished without finding a winning sequence. |
| 221 | *blank* | Blank line for readability; no action is performed. |
| 222 | *blank* | Blank line for readability; no action is performed. |
| 223 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 224 | <code># Dynamic Player Import:                                                                             #</code> | Comment labeling or describing the following code: Dynamic Player Import:                                                                             #. Python ignores this line. |
| 225 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 226 | *blank* | Blank line for readability; no action is performed. |

### Discovering player modules

| Line | Source | Explanation |
| --- | --- | --- |
| 227 | <code>def import_players() -&gt; Dict[str, player_callable]:</code> | Defines player discovery, returning a dictionary that maps player names to their play functions. |
| 228 | <code>&#x27;&#x27;&#x27; Dynamically loads players. &#x27;&#x27;&#x27;</code> | Explanatory string describing this function; it does not itself perform the described action. |
| 229 | *blank* | Blank line for readability; no action is performed. |
| 230 | <code># imports inside the function in order to avoid overhead:</code> | Comment labeling or describing the following code: imports inside the function in order to avoid overhead:. Python ignores this line. |
| 231 | <code>import os</code> | Imports filesystem operations for listing the current folder. |
| 232 | <code>import re</code> | Imports regular expressions for recognizing player filenames. |
| 233 | <code>import importlib.util</code> | Imports helpers that load a Python module from a file path. |
| 234 | *blank* | Blank line for readability; no action is performed. |
| 235 | <code># we are looking for any python script that starts with &quot;player_&quot;</code> | Comment labeling or describing the following code: we are looking for any python script that starts with "player_". Python ignores this line. |
| 236 | <code>player_expression = re.compile(r&quot;player_(?P&lt;name&gt;\S+)\.py&quot;)</code> | Compiles a pattern: player_ is literal, (?P<name>...) captures a name, \S+ means one or more non-whitespace characters, and \.py matches the extension. The r prefix makes this a raw string. Because there is no end anchor, the pattern can also match the beginning of a longer filename. |
| 237 | *blank* | Blank line for readability; no action is performed. |
| 238 | <code># find and import players:</code> | Comment labeling or describing the following code: find and import players:. Python ignores this line. |
| 239 | <code>players = {}</code> | Creates the dictionary that will hold discovered player functions. |
| 240 | <code>for file in os.listdir(&#x27;.&#x27;):</code> | Lists entries in the current working directory, not automatically the directory containing game.py. |
| 241 | <code># see if filename matches our</code> | Comment labeling or describing the following code: see if filename matches our. Python ignores this line. |
| 242 | <code>m = player_expression.match(file)</code> | Tries to match the filename pattern at the start of the current filename; returns a match object or None. |
| 243 | *blank* | Blank line for readability; no action is performed. |
| 244 | <code>if m is not None:</code> | Only attempts an import when a match was found. |
| 245 | <code>try:</code> | Starts error handling around importing this one player. |
| 246 | <code># create spec:</code> | Comment labeling or describing the following code: create spec:. Python ignores this line. |
| 247 | <code>player_spec = importlib.util.spec_from_file_location(m[&#x27;name&#x27;], file)</code> | Builds a module-loading specification from the captured player name and file path. |
| 248 | *blank* | Blank line for readability; no action is performed. |
| 249 | <code># load module:</code> | Comment labeling or describing the following code: load module:. Python ignores this line. |
| 250 | <code>player_module = importlib.util.module_from_spec(player_spec)</code> | Creates a new module object using that specification. |
| 251 | <code>player_spec.loader.exec_module(player_module)</code> | Executes the module's top-level code to populate its functions and other definitions. |
| 252 | *blank* | Blank line for readability; no action is performed. |
| 253 | <code># add player to output:</code> | Comment labeling or describing the following code: add player to output:. Python ignores this line. |
| 254 | <code>players[m[&#x27;name&#x27;]] = player_module.play</code> | Looks up its play attribute and stores it under the captured name. For player_ai.py, the dictionary key is ai. This line does not verify the function signature. |
| 255 | *blank* | Blank line for readability; no action is performed. |
| 256 | <code>except Exception as e: print(f&quot;Unable to load player \&quot;{m[&#x27;name&#x27;]}\&quot;: {e}&quot;)</code> | Reports an import or missing-attribute error and continues scanning other files. |
| 257 | *blank* | Blank line for readability; no action is performed. |
| 258 | <code>return players</code> | Returns the discovered name-to-function mapping. |
| 259 | *blank* | Blank line for readability; no action is performed. |
| 260 | *blank* | Blank line for readability; no action is performed. |
| 261 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 262 | <code># Main Function:                                                                                     #</code> | Comment labeling or describing the following code: Main Function:                                                                                     #. Python ignores this line. |
| 263 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 264 | *blank* | Blank line for readability; no action is performed. |

### Interactive entry point

| Line | Source | Explanation |
| --- | --- | --- |
| 265 | <code>if __name__ == &quot;__main__&quot;:</code> | Runs the interactive program only when game.py is executed directly. Importing it defines the class and functions without starting the prompts. |
| 266 | <code># import and list available players:</code> | Comment labeling or describing the following code: import and list available players:. Python ignores this line. |
| 267 | <code>players = import_players()</code> | Discovers players and saves the dictionary. |
| 268 | <code>print(&#x27;\nAvailable Players:&#x27;)</code> | Prints a heading for the available player names. |
| 269 | <code>for player in players:</code> | Iterates through dictionary keys, which are player names here. This player variable is a string, unlike the integer player variable inside start. |
| 270 | <code>print(f&#x27; -&gt; {player}&#x27;)</code> | Prints the current name preceded by an arrow. |
| 271 | *blank* | Blank line for readability; no action is performed. |
| 272 | <code># select player 1:</code> | Comment labeling or describing the following code: select player 1:. Python ignores this line. |
| 273 | <code>player1 = None</code> | Marks player 1 as not selected yet. |
| 274 | <code>while player1 is None:</code> | Repeats until a player function has been selected. |
| 275 | <code>try: player1 = players[input(&#x27;\nSelect player 1 (o): &#x27;)]</code> | Reads a name from input and looks up the corresponding function in players, storing it as player1. |
| 276 | <code>except KeyError as e: print(f&#x27;Input {e} not allowed.&#x27;)</code> | For an unknown name, prints the KeyError and lets the selection loop try again. |
| 277 | *blank* | Blank line for readability; no action is performed. |
| 278 | <code># select player 2:</code> | Comment labeling or describing the following code: select player 2:. Python ignores this line. |
| 279 | <code>player2 = None</code> | Marks player 2 as not selected yet. |
| 280 | <code>while player2 is None:</code> | Repeats until player 2 has a selected function. |
| 281 | <code>try: player2 = players[input(&#x27;\nSelect player 2 (x): &#x27;)]</code> | Reads player 2's name and retrieves the corresponding function. |
| 282 | <code>except KeyError as e: print(f&#x27;Input {e} not allowed.&#x27;)</code> | Reports an unknown player name and repeats the prompt. |
| 283 | *blank* | Blank line for readability; no action is performed. |
| 284 | <code># enter timeout:</code> | Comment labeling or describing the following code: enter timeout:. Python ignores this line. |
| 285 | <code>timeout = -1</code> | Initializes timeout to a negative sentinel so the prompt loop runs. |
| 286 | <code>while timeout &lt; 0:</code> | Repeats while the value is negative. Ordinary non-negative input exits the loop. |
| 287 | <code>try: timeout = float(input(&#x27;\nEnter the move timeout in seconds (0 for no timeout): &#x27;))</code> | Reads text and converts it to a floating-point number of seconds. Zero disables timing enforcement. |
| 288 | <code>except Exception as e: print(e)</code> | Prints conversion/input errors and allows another attempt. This is basic validation, not a check for finite values such as NaN. |
| 289 | *blank* | Blank line for readability; no action is performed. |
| 290 | <code># enter number of rounds:</code> | Comment labeling or describing the following code: enter number of rounds:. Python ignores this line. |
| 291 | <code>n_rounds = 0</code> | Initializes the round count to zero to force at least one prompt. |
| 292 | <code>while n_rounds &lt;= 0:</code> | Repeats until the count is a positive integer. |
| 293 | <code>try: n_rounds = int(input(&#x27;\nEnter the number of rounds: &#x27;))</code> | Reads the round count and converts the input text to an integer. |
| 294 | <code>except Exception as e: print(e)</code> | Prints input/conversion errors and retries. |
| 295 | *blank* | Blank line for readability; no action is performed. |
| 296 | <code># play for three rounds:</code> | Comment says three rounds, but the code below actually runs the user-entered n_rounds. It is an outdated comment. |
| 297 | <code>rounds = []</code> | Creates a list to store the result of each round. |
| 298 | <code>for i in range(n_rounds):</code> | Repeats n_rounds times. The loop index i is not needed to configure the game. |
| 299 | <code>size = random.randint(3, 10)</code> | Chooses a square board size from 3 through 10, inclusive. |
| 300 | <code>game = TicTacToe(</code> | Begins constructing a fresh game object for this round. |
| 301 | <code>n_cols=size,</code> | Sets its number of columns to the selected size. |
| 302 | <code>n_rows=size,</code> | Sets its number of rows to the same size. |
| 303 | <code>n_target=random.randint(3, size),</code> | Chooses the winning target from 3 through size, inclusive. This value is stored on the game object but is not passed to player callbacks. |
| 304 | <code>timeout=timeout</code> | Passes in the timeout chosen by the user. |
| 305 | <code>)</code> | Closes the multiline constructor call. |
| 306 | <code>result = game.start(</code> | Begins calling start to play this round and save its returned result. |
| 307 | <code>player1=player1,</code> | Passes the selected player 1 function. |
| 308 | <code>player2=player2</code> | Passes the selected player 2 function; the same function may be selected for both players. |
| 309 | <code>)</code> | Closes the start call. That call finishes only when the round ends or an uncaught error occurs. |
| 310 | <code>rounds.append(result)</code> | Adds the round's (winner, timings0, timings1) tuple to the results list. |
| 311 | *blank* | Blank line for readability; no action is performed. |
| 312 | <code># print game statistics:</code> | Comment labeling or describing the following code: print game statistics:. Python ignores this line. |
| 313 | <code>winner = int(sum([w for w, _, _ in rounds]) &gt; (.5 * len(rounds)))</code> | Extracts winner IDs from all results. Summing 0/1 IDs counts player 2's wins. Player 2 wins overall only if that count is greater than half the rounds; a tie selects player 1. _ names mark unused timing values. |
| 314 | <code>print(f&#x27;\nPlayer {winner + 1:d} wins the game!\n\nSummary:&#x27;)</code> | Prints the overall winner and a summary heading. |
| 315 | <code>for i, (winner, t1, t2) in enumerate(rounds):</code> | Enumerates results and unpacks each into winner and the two timing lists. This reuses winner for the current round, replacing its earlier overall value. |
| 316 | <code>print(f&#x27;  Game {i+1:d}:&#x27;)</code> | Prints the one-based round number. |
| 317 | <code>print(f&#x27;    Winner: player {winner + 1:d}&#x27;)</code> | Prints that round's winner as a one-based player number. |
| 318 | <code>print(f&#x27;    Time player 1: {sum(t1)/len(t1)*1000.:.2f} ms&#x27;)</code> | Prints player 1's average time in milliseconds to two decimal places. Unlike line 121, it has no empty-list guard; an early callback exception can make this divide by zero. |
| 319 | <code>print(f&#x27;    Time player 2: {sum(t2)/len(t2)*1000.:.2f} ms&#x27;)</code> | Prints player 2's average with the same empty-list limitation. |
| 320 | <code>print()</code> | Prints a blank line between round summaries. |

## Current behavior and limitations

These observations describe the current code; this guide does not modify it.

- The AI follows a fixed plan and then random choices. It prints the board but does not analyze positions, detect threats, or search future moves.
- The player callback receives no winning target `m`. `game.target` knows it, but `play(board, choices, player, memory)` does not. The board length reveals the number of columns; the supplied main program happens to use square boards. Do not assume the target can be recovered from the current pieces.
- The constructor defaults to 5 by 5 with target 5; the CLI overrides these with random sizes and targets for each round.
- Timeout is enforced after a callback returns, not while it is running. A callback that hangs cannot be stopped by this check. Debug output and argument copying count toward the measured duration.
- A full board is decided by average move time, not recorded as a draw. Equal averages favor player 1; an equal count of round wins also favors player 1.
- The one-line comment about playing three rounds is outdated: the input controls the round count.
- Some explanatory strings say memory comes from the previous round. The actual behavior is previous turn, with reset each new round.
- Most callback exceptions award the round to the opponent, but the final summary can then divide by zero if a timing list is empty. Malformed non-integer moves may also fail while printing the illegal-move message. These are existing limitations, not behavior fixed by this guide.
- Player loading executes Python modules found in the working folder. A matching filename alone does not guarantee a valid callable or correct signature.

## Related guides

- [player_ai.py](player_ai_EXPLAINED.md)
- [player_human.py](player_human_EXPLAINED.md)
- [player_random.py](player_random_EXPLAINED.md)
