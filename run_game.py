"""Optional launcher that leaves game.py untouched and automates AI vs random."""

import random
import game


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
        timeout, rounds = 1.0, 30
        print("\nAutomated match: using 1 second per move and 3 rounds.")
    else:
        timeout = float(input("\nEnter the move timeout in seconds (0 for no timeout): "))
        rounds = int(input("\nEnter the number of rounds: "))
    results = []
    wip_wins = 0

    for round_number in range(rounds):
        size = random.randint(3, 10)
        g = game.TicTacToe(size, size, random.randint(3, size), timeout)
        result = g.start(players[first], players[second])
        results.append(result)

        if result[0] == 0:
            wip_wins += 1

        winrate = (wip_wins / (round_number + 1)) * 100
        print(f"Round {round_number + 1}: WIP winrate: {winrate:.2f}%")
    winner = int(sum(w for w, _, _ in results) > len(results) / 2)
    print(f"\nPlayer {winner + 1} wins the game!")


if __name__ == "__main__":
    main()
