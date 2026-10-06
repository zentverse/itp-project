
"""Optional launcher that leaves game.py untouched and automates AI vs random."""

import random
import time
import game


def time_player(player, player_name):
    """Wrap player_test so that the time for every move is printed."""

    if player_name != "player_test":
        return player

    original_make_move = player.make_move

    def timed_make_move(*args, **kwargs):
        start_time = time.perf_counter()

        move = original_make_move(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time

        print(
            f"[player_test] Move took {elapsed_time:.6f} seconds"
        )

        return move

    player.make_move = timed_make_move

    return player


def main():
    players = game.import_players()

    print("\nAvailable Players:")
    for name in players:
        print(" ->", name)

    first = input("\nSelect player 1 (o): ")
    second = input("\nSelect player 2 (x): ")

    if first not in players or second not in players:
        raise SystemExit("Unknown player name.")

    if "human" not in (first, second):
        timeout = 1.0
        rounds = random.randint(1, 50)

        print(
            f"\nAutomated match: using 1 second per move "
            f"and {rounds} rounds."
        )
    else:
        timeout = float(
            input(
                "\nEnter the move timeout in seconds "
                "(0 for no timeout): "
            )
        )

        rounds = int(
            input("\nEnter the number of rounds: ")
        )

    results = []
    wip_wins = 0

    # Wrap player_test before starting the games.
    if first == "player_test":
        players[first] = time_player(
            players[first],
            first
        )

    if second == "player_test":
        players[second] = time_player(
            players[second],
            second
        )

    for round_number in range(rounds):
        size = random.randint(3, 10)

        g = game.TicTacToe(
            size,
            size,
            random.randint(3, size),
            timeout
        )

        results.append(
            g.start(
                players[first],
                players[second]
            )
        )

    print(f"\nRounds played: {len(results)}")

    wins = [0, 0]

    print("Win rate after each round:")

    for round_number, (round_winner, _, _) in enumerate(
        results,
        start=1
    ):
        wins[round_winner] += 1

        print(
            f"Round {round_number}: "
            f"Player {round_winner + 1} won"
        )

        player1_rate = wins[0] / round_number * 100
        player2_rate = wins[1] / round_number * 100

        print(
            f"  Round {round_number}: "
            f"Player 1 {player1_rate:.1f}% "
            f"({wins[0]} wins), "
            f"Player 2 {player2_rate:.1f}% "
            f"({wins[1]} wins)"
        )

    winner = int(
        sum(w for w, _, _ in results) > len(results) / 2
    )

    print(f"\nPlayer {winner + 1} wins the game!")


if __name__ == "__main__":
    main()