# WordleSolver
Wordle is a very popular word game available online from https://www.powerlanguage.co.uk/wordle/. 

For foreign speakers the game can be intimidating, because it can be hard to guess the right words, this tool tries to help solve the problem.

# How to play

1. `python3 wordlesolver.py`
1. Enter your guess at https://www.powerlanguage.co.uk/wordle/ and submit
1. In the wordlesolver.py type your guess
1. You will be asked for all "green tiles"
1. Then you will be asked for all "yellow tiles"
1. Should your green tiles show up multiple times within your guess, you will be asked to identify the correct location as a numeric value from 1 - 5
1. The script will now suggest either common or not so common (uncommon) words
1. Continue until you win - end the program with the word win

# What it doens't do

This script does **not know** or **lookup** the solution. While looking up the solution it is trivial from the browser console in the online game that would be absolutely no fun. 

# Could this be better

WAY better, but it does the job for now :)