import random
from typing import Any, List, Tuple

def play(board:List[List[int]], choices:List[int], player:int, memory:Any) -> Tuple[int, Any]:    
   
    print('board===>',board)
    print('choices===>',choices)
    print('memory===>',memory)
    '''Your team's player.                                                                        
                                                                                                   
         Arguments:                                                                                
             board (List[List[int]]): The game plan as a list of columns. Each column is a list of
                                      integer ids signifying the player who placed the piece.      
             choices     (List[int]): The possible moves allowed by the game rules.                
             player            (int): Integer id of the current player in the game plan.          
             memory            (any): Persistent information passed as the second output in the    
                                      previous round. Initialized with None.                      
                                                                                                   
         Returns   (Tuple[int, Any]): A tuple of the selected column (int) and the memory object  
                                      for the next iteration (can be anything).                    
     '''                                                                                          
     # your code goes here:
     #
     # first move
    #  if memory is None:
    #      # choose a random column from the available choices
    #      return random.choice(choices), memory

         # Column indexes start at 0:
     # 0 = first column, 1 = second column, etc.
    planned_moves = [2, 2, 1, 3, 0]

     # On our first turn, start at the beginning.
    if memory is None:
         memory = 0

     # Find the next planned move that is allowed.
    while memory < len(planned_moves):
         move = planned_moves[memory]
         memory += 1

         if move in choices:
             return move, memory

     # If the plan is finished, choose any available column.
    return random.choice(choices), memory



# Random-move example:
# def play(board, choices, player, memory):
#     move = random.choice(choices)
#     return move, memory