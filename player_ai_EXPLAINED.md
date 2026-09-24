# player_ai.py — Line-by-Line Explanation

The team player: a fixed sequence of planned moves, a memory index, and a random fallback.

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

Source: [player_ai.py](player_ai.py). 53 lines.


### Imports and callback

| Line | Source | Explanation |
| --- | --- | --- |
| 1 | <code>import random</code> | Imports the standard-library random module. Its functions select random moves, board sizes, or a starting player. |
| 2 | <code>from typing import Any, List, Tuple</code> | Imports type-hint names: Any accepts any kind of value, List describes a list, and Tuple describes a fixed collection of returned values. Hints do not enforce types at runtime. |
| 3 | *blank* | Blank line for readability; no action is performed. |
| 4 | <code>def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -&gt; Tuple[int, Any]:</code> | Defines the player callback with the required four inputs and two-item return type. board is a list of columns, choices contains legal zero-based indices, player is 0 or 1, and memory is the saved state from this player's previous turn. |
| 5 | *blank* | Blank line for readability; no action is performed. |
| 6 | <code>print(&#x27;board===&gt;&#x27;,board)</code> | Prints the incoming board for debugging; this takes place on every AI turn. |
| 7 | <code>print(&#x27;choices===&gt;&#x27;,choices)</code> | Prints the currently legal column indices. |
| 8 | <code>print(&#x27;memory===&gt;&#x27;,memory)</code> | Prints the incoming memory before this turn changes it. |
| 9 | <code>&#x27;&#x27;&#x27;Your team&#x27;s player.</code> | Starts a multiline explanatory string. Because print statements precede it, Python does not treat it as this function's docstring. |
| 10 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 11 | <code>Arguments:</code> | Introduces the parameter descriptions in the explanatory string. |
| 12 | <code>board (List[List[int]]): The game plan as a list of columns. Each column is a list of</code> | Description of the board input: a list of columns containing player IDs from bottom to top. |
| 13 | <code>integer ids signifying the player who placed the piece.</code> | Continues the board description: stored numbers identify who placed each piece. |
| 14 | <code>choices     (List[int]): The possible moves allowed by the game rules.</code> | Description of choices: the legal zero-based columns for the current turn. |
| 15 | <code>player            (int): Integer id of the current player in the game plan.</code> | Documents a player argument: callbacks choose moves; integer player IDs identify which pieces belong to the current player. |
| 16 | <code>memory            (any): Persistent information passed as the second output in the</code> | Description of persistent player state. In this engine it is retained between turns by the same player and reset for each new round. |
| 17 | <code>previous round. Initialized with None.</code> | The text says previous round, but the engine actually passes memory from the previous turn by this player; new rounds reset it to None. |
| 18 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 19 | <code>Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object</code> | Description of persistent player state. In this engine it is retained between turns by the same player and reset for each new round. |
| 20 | <code>for the next iteration (can be anything).</code> | Documents the returned pair: selected column and state for the next turn. |
| 21 | <code>&#x27;&#x27;&#x27;</code> | Closes the multiline explanatory string. |
| 22 | <code># your code goes here:</code> | Comment labeling or describing the following code: your code goes here:. Python ignores this line. |
| 23 | <code>#</code> | Comment separator for readability; Python ignores it. |
| 24 | <code># first move</code> | Comment labeling or describing the following code: first move. Python ignores this line. |
| 25 | <code>#  if memory is None:</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |
| 26 | <code>#      # choose a random column from the available choices</code> | Comment labeling or describing the following code: # choose a random column from the available choices. Python ignores this line. |
| 27 | <code>#      return random.choice(choices), memory</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |
| 28 | *blank* | Blank line for readability; no action is performed. |
| 29 | <code># Column indexes start at 0:</code> | Comment labeling or describing the following code: Column indexes start at 0:. Python ignores this line. |
| 30 | <code># 0 = first column, 1 = second column, etc.</code> | Comment labeling or describing the following code: 0 = first column, 1 = second column, etc.. Python ignores this line. |

### Fixed plan and persistent memory

| Line | Source | Explanation |
| --- | --- | --- |
| 31 | <code>planned_moves = [2, 2, 1, 3, 0]</code> | Creates the fixed sequence of zero-based column indices. For a human, these are columns 3, 3, 2, 4, 1. It is recreated on each call; memory remembers the position in the sequence. |
| 32 | *blank* | Blank line for readability; no action is performed. |
| 33 | <code># On our first turn, start at the beginning.</code> | Comment labeling or describing the following code: On our first turn, start at the beginning.. Python ignores this line. |
| 34 | <code>if memory is None:</code> | Checks whether this player has no saved state yet. is None tests for the None sentinel; it does not treat integer zero as missing. |
| 35 | <code>memory = 0</code> | Starts the next-plan index at zero on the first turn. |
| 36 | *blank* | Blank line for readability; no action is performed. |
| 37 | <code># Find the next planned move that is allowed.</code> | Comment labeling or describing the following code: Find the next planned move that is allowed.. Python ignores this line. |
| 38 | <code>while memory &lt; len(planned_moves):</code> | Continues looking through the plan while the index is below its length, which is five. |
| 39 | <code>move = planned_moves[memory]</code> | Reads the planned column at the current index. memory is an index into planned_moves, while move is an index into board. |
| 40 | <code>memory += 1</code> | Advances the plan index before checking legality. Therefore even an unavailable planned move is consumed and skipped. |
| 41 | *blank* | Blank line for readability; no action is performed. |
| 42 | <code>if move in choices:</code> | Checks whether this planned column is in the supplied legal choices. This rejects full columns and columns that do not exist on a smaller board. |
| 43 | <code>return move, memory</code> | Returns the legal move and next-plan index as a tuple. return ends the function immediately; game.py stores the index for this player's next turn. |
| 44 | *blank* | Blank line for readability; no action is performed. |
| 45 | <code># If the plan is finished, choose any available column.</code> | Comment labeling or describing the following code: If the plan is finished, choose any available column.. Python ignores this line. |
| 46 | <code>return random.choice(choices), memory</code> | If the plan is exhausted, chooses a random legal column and returns the unchanged memory index. Future turns will continue to use this fallback. The engine only calls the function when choices is nonempty. |
| 47 | *blank* | Blank line for readability; no action is performed. |
| 48 | *blank* | Blank line for readability; no action is performed. |

### Commented example

| Line | Source | Explanation |
| --- | --- | --- |
| 49 | *blank* | Blank line for readability; no action is performed. |
| 50 | <code># Random-move example:</code> | Comment labeling or describing the following code: Random-move example:. Python ignores this line. |
| 51 | <code># def play(board, choices, player, memory):</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |
| 52 | <code>#     move = random.choice(choices)</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |
| 53 | <code>#     return move, memory</code> | Disabled example code inside a comment; it does not execute. It illustrates an alternative random-move implementation, not the active fixed plan. |

## Memory worked example

`memory` is a value passed back and forth, not an automatic record of the board or a database. The player returns it; the engine saves it and supplies it on that same player's next turn.

The active sequence in `player_ai.py` is:

```python
planned_moves = [2, 2, 1, 3, 0]
```

Assume a board of at least four columns and that all planned moves remain legal:

| AI turn | Incoming memory | Operation | Returned pair | Human column number |
| --- | --- | --- | --- | --- |
| 1 | `None` | Initialize to 0; read plan index 0; advance to 1. | `(2, 1)` | 3 |
| 2 | `1` | Read plan index 1; advance to 2. | `(2, 2)` | 3 |
| 3 | `2` | Read plan index 2; advance to 3. | `(1, 3)` | 2 |
| 4 | `3` | Read plan index 3; advance to 4. | `(3, 4)` | 4 |
| 5 | `4` | Read plan index 4; advance to 5. | `(0, 5)` | 1 |
| 6 onward | `5` | The while condition is false, so select randomly from choices. | `(random_legal_column, 5)` | Depends on the move. |

A real round may end before all six turns occur.


### When a planned move is unavailable

Suppose the AI receives `memory = 1` and `choices = [0, 1, 3]`. It reads `planned_moves[1]`, which is 2, then advances memory to 2. Column 2 is not allowed, so the loop continues **during the same turn**. It reads `planned_moves[2]`, which is 1, advances memory to 3, and returns `(1, 3)`. One move was played, but two plan entries were consumed.

On a three-column board, the planned column index 3 does not exist. The same membership check skips it safely.


### Where the value is saved

For player ID 0, this engine statement is effectively:

```python
move, memory[0] = player_function(board_copy, choices_copy, 0, memory[0])
```

The engine's `memory` is a two-item list of player states. Inside `player_ai.play`, the parameter named `memory` is just this player's value, such as integer 3. These are different local variables with the same name.

If both players use `ai`, they share the function but have separate saved indices. At the start of a new round, `memory = [None, None]` resets both. If the AI incremented its local index but did not return it, the engine would not receive that updated integer.

## Related guides

- [game.py](game_EXPLAINED.md)
- [player_human.py](player_human_EXPLAINED.md)
- [player_random.py](player_random_EXPLAINED.md)
