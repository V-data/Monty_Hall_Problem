#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:02:26 2021

@author: Platino
"""

import random


def user_prompt(prompt, default=None):
    """ Allow use os default values in imput. """
    prompt = '{} [{}]: '.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response


# input number of times to run simulation.
# each run represent a person playing the game once.
num_runs = int(user_prompt("Input number of runs", 20000))

# assign counters for way to win
first_choice_wins = 0
pick_change_wins = 0
doors = ['a', 'b', 'c']

# run Monte Carlo.
for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)

    if pick == winner:
        first_choice_wins += 1
    else:
        pick_change_wins += 1


print(f"Wins with original pick = {first_choice_wins}")
print(f"Wins with change pick = {pick_change_wins}")
print("Probability of winning with initial guess: {:.2f}"
      .format(first_choice_wins / num_runs))
print("Probability of winning by switching: {:.2f}"
      .format(pick_change_wins / num_runs))

input("\nPress Enter key to exit.")
