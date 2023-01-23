PAPER = "P"
SCISSORS = "S"
ROCK = "R"
init_play = prev_play = "S"
ideal_res = {PAPER: ROCK, ROCK: SCISSORS, SCISSORS: PAPER}
opponent_list = [False, False, False, False]
opponent_counter = -1
history = []
play_order = [
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
]


def player(prev_opponent, opponent_history=[]):
    global history, prev_play, opponent_list, ideal_res, opponent_counter, play_order
    opponent_history.append(prev_opponent)
    history.append(prev_play)

    if len(set(opponent_list)) == 1 and opponent_history[-5:] == [
        ROCK,
        PAPER,
        PAPER,
        SCISSORS,
        ROCK,
    ]:
        opponent_list[0] = True

    if opponent_list[0]:
        if len(opponent_history) % 1000 == 0:
            opponent_list = [True, True, True, True]
            opponent_history.clear()

        opponent_list = [PAPER, SCISSORS, SCISSORS, ROCK, PAPER]
        opponent_counter = (opponent_counter + 1) % 5
        return opponent_list[opponent_counter]

    if len(set(opponent_list)) == 1 and opponent_history[-5:] == [
        PAPER,
        PAPER,
        ROCK,
        ROCK,
        ROCK,
    ]:
        opponent_list[1] = True

    if opponent_list[1]:
        last_two = "".join(history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1
        potential_plays = [
            prev_play + ROCK,
            prev_play + PAPER,
            prev_play + SCISSORS,
        ]
        sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}
        prediction = max(sub_order, key=sub_order.get)[-1:]

        if len(opponent_history) % 1000 == 0:
            opponent_list = [False, False, False, False]
            opponent_history.clear()
            play_order = [
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
            ]

        prev_play = ideal_res[prediction]
        return prev_play

    # kris
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == [
        PAPER,
        ROCK,
        ROCK,
        ROCK,
        ROCK,
    ]:
        opponent_list[2] = True

    if opponent_list[2]:
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False, False, False, False]
            opponent_history.clear()

        prev_play = ideal_res[prev_play]
        return prev_play

    # mrugesh
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == [
        ROCK,
        ROCK,
        ROCK,
        ROCK,
        ROCK,
    ]:
        opponent_list[3] = True

    if opponent_list[3]:
        if len(opponent_history) == 1000:
            opponent_list = [False, False, False, False]
            opponent_history.clear()

        last_ten = history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        prev_play = ideal_res[most_frequent]
        return prev_play

    prev_play = init_play
    return
