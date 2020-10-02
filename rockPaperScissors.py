"""
Problem statement: Write a function to simulate the rock, paper, scissors game between Abigail and Benson.
Problem Link: https://edabit.com/challenge/p6uXeD7JC7cmxeD2Z

Abigail and Benson are playing Rock, Paper, Scissors.

Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played.

Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

R stands for Rock
P stands for Paper
S stands for Scissors

Examples
calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"

# Ben wins the first game (Paper beats Rock).
# Abigail wins the second game (Rock beats Scissors).
# Abigail wins the third game (Scissors beats Paper).
# Abigail wins 2/3.

calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"

calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"
"""


def first_player_wins(a, b):
    """
    If tie                    : Returns  0
    If first player wins      : Returns  1
    If second player wins     : Returns -1
    """
    if a == b:
        return 0
    elif [a, b] == ["R", "S"] or [a, b] == ["S", "P"] or [a, b] == ["P", "R"]:
        return 1
    return -1


def calculate_score(game):
    abigail = benson = 0
    for turn in game:
        decision = first_player_wins(turn[0], turn[1])
        if decision == 1:
            abigail += 1
        elif decision == -1:
            benson += 1

    if abigail == benson:
        return "Tie"
    elif abigail > benson:
        return "Abigail"
    return "Benson"

