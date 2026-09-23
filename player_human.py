#====================================================================================================#
# Imports:                                                                                           #
#====================================================================================================#

from typing import Any, List, Tuple

#====================================================================================================#
# Play Function:                                                                                     #
#====================================================================================================#

def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -> Tuple[int, Any]:
    '''A human player.
    
        Arguments:
            board (List[List[int]]): the game plan as a list of columns. Each column is a list of integer ids signifying the player who placed the piece.
            choices     (List[int]): the possible moves allowed by the game rules.
            player            (int): integer id of the current player in the game plan.
            memory            (any): persistent information passed as the second output in the previous round. Initialized with None.

        Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object for the next iteration (can be anything).
    '''

    # ask for next move:
    return int(input(f"Select a column [possible: {', '.join([str(c+1) for c in choices])}]: ")) - 1, memory