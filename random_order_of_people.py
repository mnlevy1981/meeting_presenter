#!/usr/bin/env python

"""
    Every meeting a different person from the BGC group will give a brief update on his or her work.
    Only exists so that we don't need to draw names out of a hat when the cycle is due to repeat.
"""

import os
import random
import time

# 1) Set up seeding for random number generator used to shuffle names
NOW = time.time()
SEED = int(NOW) % 10000
print(f'time.time() = {NOW} so seeding with {SEED}\n----')
random.seed(SEED)

# 2) If previous cycle was written to a file, read it back in
#    We store PREVIOUS_CYCLE_FILE_EXISTS because it determines if there are restrictions
#    to the order of the shuffling (e.g. last person can't subsequently go first)
PREVIOUS_CYCLE_FILE = 'previous_cycle.txt'
PREVIOUS_CYCLE_FILE_EXISTS = os.path.isfile(PREVIOUS_CYCLE_FILE)
if PREVIOUS_CYCLE_FILE_EXISTS:
    PREVIOUS_CYCLE = open(PREVIOUS_CYCLE_FILE, "r")
    ORIG_PEOPLE = PREVIOUS_CYCLE.read().splitlines()
    PREVIOUS_CYCLE.close()
else:
    ORIG_PEOPLE = ['Magdalena',
                   'Kristen',
                   'Mike',
                   'Keith',
                   'Matt',
                   'Precious',
                   'Dan'
                  ]

# 3) Do the shuffling and print results
PEOPLE = ORIG_PEOPLE.copy()
random.shuffle(PEOPLE)
if PREVIOUS_CYCLE_FILE_EXISTS:
    # If we read in the last cycle from a file, we want to
    # limit who can go first or second in the new cycle
    while (ORIG_PEOPLE[-1] in PEOPLE[:2]) or (ORIG_PEOPLE[-2] == PEOPLE[0]):
        print(f'Reshuffling, {PEOPLE} is not valid order')
        random.shuffle(PEOPLE)
print(f'\nOriginal list\n{ORIG_PEOPLE}')
print(f'\nShuffled list\n{PEOPLE}')

# 4) Store cycle in new file
PREVIOUS_CYCLE = open(PREVIOUS_CYCLE_FILE, "w+")
for person in PEOPLE:
    PREVIOUS_CYCLE.write(f'{person}\n')
