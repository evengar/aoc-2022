# Part 1

# dicts for storing scores

move_dict = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

results_dict = {
    "win": 6,
    "loss": 0,
    "draw": 3
}

# dict for translating input

input_dict = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

# game dict
# denotes which move defeats which

win_dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def play_rps(input1, input2):
    move1 = input_dict[input1]
    move2 = input_dict[input2]

    if win_dict[move1] == move2:
        result = "loss"
    elif win_dict[move2] == move1:
        result = "win"
    else:
        result = "draw"
    
    return(move_dict[move2] + results_dict[result])

# read data and play all games
with open("data/02-input.txt") as f:
    strategy_guide = f.readlines()

score = 0

for move in strategy_guide:
    inputs = move.strip().split(" ")
    score += play_rps(inputs[0], inputs[1])

print(score)

# Part 2

strategy_dict = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}

# create dict for lose conditions
# could probably be done differently, but easier this way
lose_dict = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

def play_rps_smarter(opponents_input, strategy):
    move1 = input_dict[opponents_input]
    tactic = strategy_dict[strategy]

    if tactic == "loss":
        move2 = win_dict[move1]
    elif tactic == "win":
        move2 = lose_dict[move1]
    else:
        move2 = move1

    return results_dict[tactic] + move_dict[move2]

score = 0

for move in strategy_guide:
    inputs = move.strip().split(" ")
    score += play_rps_smarter(inputs[0], inputs[1])

print(score)