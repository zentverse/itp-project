# player_human.py — Line-by-Line Explanation

Reads a column number from the terminal and returns a zero-based move.

Checked against the local source on September 24, 2026. Update this guide when the source changes.

The board stores columns from bottom to top. Player ID `0` is `o`; ID `1` is `x`. Legal choices are zero-based column indices.

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

Source: [player_human.py](player_human.py). 24 lines.


### Human input player

| Line | Source | Explanation |
| --- | --- | --- |
| 1 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 2 | <code># Imports:                                                                                           #</code> | Comment labeling or describing the following code: Imports:                                                                                           #. Python ignores this line. |
| 3 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 4 | *blank* | Blank line for readability; no action is performed. |
| 5 | <code>from typing import Any, List, Tuple</code> | Imports type-hint names: Any accepts any kind of value, List describes a list, and Tuple describes a fixed collection of returned values. Hints do not enforce types at runtime. |
| 6 | *blank* | Blank line for readability; no action is performed. |
| 7 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 8 | <code># Play Function:                                                                                     #</code> | Comment labeling or describing the following code: Play Function:                                                                                     #. Python ignores this line. |
| 9 | <code>#====================================================================================================#</code> | Comment separator for readability; Python ignores it. |
| 10 | *blank* | Blank line for readability; no action is performed. |
| 11 | <code>def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -&gt; Tuple[int, Any]:</code> | Defines the required play callback. board is column-oriented game data; choices lists legal zero-based moves; player is the current ID; memory is this player's saved state. Returns a pair of move and memory; annotations describe types without enforcing them. |
| 12 | <code>&#x27;&#x27;&#x27;A human player.</code> | Explanatory string describing this function; it does not itself perform the described action. |
| 13 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 14 | <code>Arguments:</code> | Introduces the parameter descriptions in the explanatory string. |
| 15 | <code>board (List[List[int]]): the game plan as a list of columns. Each column is a list of integer ids signifying the player who placed the piece.</code> | Description of the board input: a list of columns containing player IDs from bottom to top. |
| 16 | <code>choices     (List[int]): the possible moves allowed by the game rules.</code> | Description of choices: the legal zero-based columns for the current turn. |
| 17 | <code>player            (int): integer id of the current player in the game plan.</code> | Documents a player argument: callbacks choose moves; integer player IDs identify which pieces belong to the current player. |
| 18 | <code>memory            (any): persistent information passed as the second output in the previous round. Initialized with None.</code> | Documents saved state. Despite saying previous round, memory comes from this player's previous turn and is reset at the start of a new round. |
| 19 | *blank* | Blank line within the multiline explanation; no game action is performed. |
| 20 | <code>Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object for the next iteration (can be anything).</code> | Description of persistent player state. In this engine it is retained between turns by the same player and reset for each new round. |
| 21 | <code>&#x27;&#x27;&#x27;</code> | Closes the multiline explanatory string. |
| 22 | *blank* | Blank line for readability; no action is performed. |
| 23 | <code># ask for next move:</code> | Comment labeling or describing the following code: ask for next move:. Python ignores this line. |
| 24 | <code>return int(input(f&quot;Select a column [possible: {&#x27;, &#x27;.join([str(c+1) for c in choices])}]: &quot;)) - 1, memory</code> | Builds the prompt by adding 1 to every legal index, converting each to text, and joining with commas. input reads text; int converts it; subtracting 1 converts the human column number back to a zero-based move. Returns that move and unchanged memory. Non-numeric input raises ValueError; illegal numbers are rejected by the engine rather than re-prompted here. |

## Input example

With `choices = [0, 2]`, the prompt lists columns `1, 3`. Typing `3` returns `(2, memory)`. Non-numeric input raises an exception; a number outside the legal choices is rejected by the engine. This function does not retry invalid input.

## Related guides

- [game.py](game_EXPLAINED.md)
- [player_ai.py](player_ai_EXPLAINED.md)
- [player_random.py](player_random_EXPLAINED.md)
