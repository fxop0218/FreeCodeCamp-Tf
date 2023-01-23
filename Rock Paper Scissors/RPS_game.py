# DO NOT MODIFY THIS FILE

import random

TIE = "tie"
P2 = "p2"
P1 = "p1"
PAPER = "P"
SCISSORS = "S"
ROCK = "R"


def play(player1, player2, num_games, verbose=False):
    p1_p_play = ""
    p2_p_play = ""
    results = {P1: 0, P2: 0, TIE: 0}

    for _ in range(num_games):
        p1_play = player1(p2_p_play)
        p2_play = player2(p1_p_play)

        if p1_play == p2_play:
            results[TIE] += 1
            winner = "Tie."
        elif (
            (p1_play == PAPER and p2_play == ROCK)
            or (p1_play == ROCK and p2_play == SCISSORS)
            or (p1_play == SCISSORS and p2_play == PAPER)
        ):
            results[P1] += 1
            winner = "Player1 wins."
        elif (
            p2_play == PAPER
            and p1_play == ROCK
            or p2_play == ROCK
            and p1_play == SCISSORS
            or p2_play == SCISSORS
            and p1_play == PAPER
        ):
            results[P2] += 1
            winner = "Player2 wins."

        if verbose:
            print("Player 1:", p1_play, "\n Player 2:", p2_play)
            print(winner)
            print()

        p1_p_play = p1_play
        p2_p_play = p2_play

    games_won = results[P2] + results[P1]

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results[P1] / games_won * 100

    print("Results:", results)
    print(f"Player1 WR: {win_rate}%")

    return win_rate


def quincy(prev_play, counter=[0]):

    counter[0] += 1
    choices = [ROCK, ROCK, PAPER, PAPER, SCISSORS]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == "":
        most_frequent = SCISSORS

    ideal_response = {PAPER: SCISSORS, ROCK: PAPER, SCISSORS: ROCK}
    return ideal_response[most_frequent]


def kris(prev_opponent_play):
    if prev_opponent_play == "":
        prev_opponent_play = ROCK
    ideal_response = {PAPER: SCISSORS, ROCK: PAPER, SCISSORS: ROCK}
    return ideal_response[prev_opponent_play]


def abbey(
    prev_opponent_play,
    opponent_history=[],
    play_order=[
        {
            "RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
        }
    ],
):

    if not prev_opponent_play:
        prev_opponent_play = ROCK
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + ROCK,
        prev_opponent_play + PAPER,
        prev_opponent_play + SCISSORS,
    ]

    sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {PAPER: SCISSORS, ROCK: PAPER, SCISSORS: ROCK}
    return ideal_response[prediction]


def human(prev_opponent_play):
    play = ""
    while play not in [ROCK, PAPER, SCISSORS]:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play


def random_player(prev_opponent_play):
    return random.choice([ROCK, PAPER, SCISSORS])
