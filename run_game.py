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
    automated = {first, second} == {"ai", "random"}
    if automated:
        timeout, rounds = 1.0, 3
        print("\nAI vs random: using 1 second per move and 3 rounds.")
    else:
        timeout = float(input("\nEnter the move timeout in seconds (0 for no timeout): "))
        rounds = int(input("\nEnter the number of rounds: "))
    results = []
    for _ in range(rounds):
        size = random.randint(3, 10)
        g = game.TicTacToe(size, size, random.randint(3, size), timeout)
        results.append(g.start(players[first], players[second]))
    winner = int(sum(w for w, _, _ in results) > len(results) / 2)
    print(f"\nPlayer {winner + 1} wins the game!")


if __name__ == "__main__":
    main()
