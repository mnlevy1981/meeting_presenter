#!/usr/bin/env python

"""
    Every meeting a different person from the BGC group will give a brief update on his or her work.
    Only exists so that we don't need to draw names out of a hat when the cycle is due to repeat.
"""

import os
import random
import time

def _get_participants_from_stdin():
    participants = ['Magdalena',
                    'Kristen',
                    'Mike',
                    'Keith',
                    'Matt',
                    'Precious',
                    'Dan'
                   ]
    return participants

if __name__ == '__main__':
    # 1) Set up seeding for random number generator used to shuffle names
    NOW = time.time()
    SEED = int(NOW) % 10000
    print(f'time.time() = {NOW} so seeding with {SEED}\n----')
    random.seed(SEED)

    # 2) If previous cycle was written to a file, read it back in
    #    We store previous_cycle_file_exists because it determines if there are restrictions
    #    to the order of the shuffling (e.g. last person can't subsequently go first)
    previous_cycle_file = 'previous_cycle.txt'
    previous_cycle_file_exists = os.path.isfile(previous_cycle_file)
    if previous_cycle_file_exists:
        previous_cycle = open(previous_cycle_file, "r")
        orig_people = previous_cycle.read().splitlines()
        previous_cycle.close()
    else:
        orig_people = _get_participants_from_stdin()

    # 3) Do the shuffling and print results
    people = orig_people.copy()
    random.shuffle(people)
    if previous_cycle_file_exists:
        # If we read in the last cycle from a file, we want to
        # limit who can go first or second in the new cycle
        while (orig_people[-1] in people[:2]) or (orig_people[-2] == people[0]):
            print(f'Reshuffling, {people} is not valid order')
            random.shuffle(people)
    print(f'\nOriginal list\n{orig_people}')
    print(f'\nShuffled list\n{people}')

    # 4) Store cycle in new file
    previous_cycle = open(previous_cycle_file, "w+")
    for person in people:
        previous_cycle.write(f'{person}\n')
