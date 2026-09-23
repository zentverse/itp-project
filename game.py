#====================================================================================================#
# Imports:                                                                                           #
#====================================================================================================#

import random
import time
import copy


#====================================================================================================#
# Typing:                                                                                            #
#====================================================================================================#

from typing import Any, List, Dict, Tuple, Callable
player_callable = Callable[[List[List[int]], List[int], int, Any], Tuple[int, Any]]


#====================================================================================================#
# Game Class:                                                                                        #
#====================================================================================================#

class TicTacToe:
    def __init__(self, n_rows:int=5, n_cols:int=5, n_target:int=5, timeout:float=0) -> None:
        '''Create a new TicTacToe game for two players.

            Arguments:
                n_rows    (int): number of rows of the board
                n_cols    (int): number of columns of the board
                n_target  (int): number of adjacent pieces needed to win
                timeout (float): time for each turn in seconds
        '''
        self.columns     = [[] for _ in range(n_cols)]
        self.max_rows    = n_rows
        self.target      = n_target
        self.timeout     = timeout

    def __repr__(self) -> str:
        '''Create some ascii-art representing the current state of the game.'''
        board = []

        # add bottom:
        board.append('└' + '─'.join(['─' for _ in self.columns]) + '┘')
        
        for i in range(self.max_rows):
            # print current row:
            row = [('o','x')[col[i]] if len(col) > i else ' ' for col in self.columns]

            # print next row:
            board.append('│' + ' '.join(row) + '│')

        # add top:
        board.append(' ' + ' '.join(['↓' for _ in self.columns]) + ' ')
        board.append(' ' + ' '.join([str(i+1) for i, col in enumerate(self.columns)]) + ' ')

        # print whole board:
        return '\n  ' + '\n  '.join(board[::-1])

    def start(self, player1:player_callable, player2:player_callable) -> Tuple[int, List[float], List[float]]:
        ''' Start a game for two players.

            Arguments:
                player1 (player_callable): a callback performing the actions of player 1.
                player2 (player_callable): a callback performing the actions of player 2.
        '''

        # game variables:
        callbacks = (player1, player2)
        memory = [None, None]
        times  = [[], []]
        player = random.randint(0,1)
        winner = -1

        # print gameplan:
        print(self)

        while winner < 0:
            # get all possible columns:
            choices = [i for i, col in enumerate(self.columns) if len(col) < self.max_rows]
            if len(choices) == 0:
                print(f'\nGame Over. Fastest player wins!')
                t0, t1 = [sum(t)/len(t) for t in times]
                winner = int(t1 < t0)
                break

            # get next player:
            player = (player + 1) % 2
            print(f"\nPlayer {player + 1:d}'s turn ({('o','x')[player]}):")

            # get next column from player (with timeout):
            t = time.time()

            try: move, memory[player] = callbacks[player](copy.deepcopy(self.columns), copy.deepcopy(choices), player, memory[player])
            except Exception as e:
                print(f'\nExeption in player {player + 1:d} code: {e}')
                winner = (player + 1) % 2
                break

            t = time.time() - t
            times[player].append(t)

            if self.timeout > 0 and t > self.timeout:
                print(f'\nPlayer {player + 1:d}\'s move timed out.')
                winner = (player + 1) % 2
                break

            if move not in choices:
                print(f'\nImpossible move by player {player + 1:d}. Column {move + 1:d} is already full.')
                winner = (player + 1) % 2
                break

            # take turn:
            self.columns[move].append(player)
            print(self)

            # check for winner:
            winner = self.check_win()

        # return winning player:
        print(f'\nPlayer {winner + 1:d} won the round!')
        for i, t in enumerate(times):
            if len(t) > 0: print(f'  Average time per turn player {i + 1:d}: {sum(t)/len(t)*1000.:.2f} ms')

        return (winner,) + tuple(times)

    def check_win(self) -> int:
        '''Check whether any of the players has `target` adjacent pieces on the board (any direction).'''

        # helper function checking single cells:
        def check_cell(i, j, last, count):
            if j >= len(self.columns[i]):
                last, count = -1, 0

            elif self.columns[i][j] == last:
                count += 1

            else: last, count = self.columns[i][j], 1

            return last, count, count >= self.target


        # vertically:
        for i in range(len(self.columns)):
            last, count = -1, 0

            for j in range(self.max_rows):
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last


        # horizontally:
        for j in range(self.max_rows):
            last, count = -1, 0
            
            for i in range(len(self.columns)):
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last


        # diagonally (up):
        for i in range(len(self.columns)):
            j, last, count = 0, -1, 0

            while i < len(self.columns) and j < self.max_rows:
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last

                i += 1
                j += 1

        for j in range(self.max_rows):
            i, last, count = 0, -1, 0

            while i < len(self.columns) and j < self.max_rows:
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last

                i += 1
                j += 1


        # diagonally (down):
        for i in range(len(self.columns)):
            j, last, count = self.max_rows-1, -1, 0

            while i < len(self.columns) and j >= 0:
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last

                i += 1
                j -= 1

        for j in range(self.max_rows):
            i, last, count = len(self.columns)-1, -1, 0

            while i >= 0 and j < self.max_rows:
                # check cell:
                last, count, win = check_cell(i, j, last, count)

                # exit on win:
                if win: return last

                i -= 1
                j += 1

        return -1


#====================================================================================================#
# Dynamic Player Import:                                                                             #
#====================================================================================================#

def import_players() -> Dict[str, player_callable]:
    ''' Dynamically loads players. '''

    # imports inside the function in order to avoid overhead:
    import os
    import re
    import importlib.util

    # we are looking for any python script that starts with "player_"
    player_expression = re.compile(r"player_(?P<name>\S+)\.py")

    # find and import players:
    players = {}
    for file in os.listdir('.'):
        # see if filename matches our 
        m = player_expression.match(file)

        if m is not None:
            try:
                # create spec:
                player_spec = importlib.util.spec_from_file_location(m['name'], file)
                
                # load module:
                player_module = importlib.util.module_from_spec(player_spec)
                player_spec.loader.exec_module(player_module)

                # add player to output:
                players[m['name']] = player_module.play

            except Exception as e: print(f"Unable to load player \"{m['name']}\": {e}")

    return players


#====================================================================================================#
# Main Function:                                                                                     #
#====================================================================================================#

if __name__ == "__main__":
    # import and list available players:
    players = import_players()
    print('\nAvailable Players:')
    for player in players:
        print(f' -> {player}')

    # select player 1:
    player1 = None
    while player1 is None:
        try: player1 = players[input('\nSelect player 1 (o): ')]
        except KeyError as e: print(f'Input {e} not allowed.')

    # select player 2:
    player2 = None
    while player2 is None:
        try: player2 = players[input('\nSelect player 2 (x): ')]
        except KeyError as e: print(f'Input {e} not allowed.')

    # enter timeout:
    timeout = -1
    while timeout < 0:
        try: timeout = float(input('\nEnter the move timeout in seconds (0 for no timeout): '))
        except Exception as e: print(e)

    # enter number of rounds:
    n_rounds = 0
    while n_rounds <= 0:
        try: n_rounds = int(input('\nEnter the number of rounds: '))
        except Exception as e: print(e)

    # play for three rounds:
    rounds = []
    for i in range(n_rounds):
        size = random.randint(3, 10)
        game = TicTacToe(
            n_cols=size,
            n_rows=size,
            n_target=random.randint(3, size),
            timeout=timeout
        )
        result = game.start(
            player1=player1,
            player2=player2
        )
        rounds.append(result)

    # print game statistics:
    winner = int(sum([w for w, _, _ in rounds]) > (.5 * len(rounds)))
    print(f'\nPlayer {winner + 1:d} wins the game!\n\nSummary:')
    for i, (winner, t1, t2) in enumerate(rounds):
        print(f'  Game {i+1:d}:')
        print(f'    Winner: player {winner + 1:d}')
        print(f'    Time player 1: {sum(t1)/len(t1)*1000.:.2f} ms')
        print(f'    Time player 2: {sum(t2)/len(t2)*1000.:.2f} ms')
        print()