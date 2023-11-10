#!/usr/bin/env python

"""
    Every meeting a different person from the BGC group will give a brief update on his or her work.
    Only exists so that we don't need to draw names out of a hat when the cycle is due to repeat.
"""

import os
import random
import time

#####################################

def _parse_args():
    """ Parse command line arguments
    """
    import argparse

    parser = argparse.ArgumentParser(description="Shuffle elements of a list",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--command-line', action='store_true', dest='cmd_line',
                        help='Flag to force user to enter list from command line')

    parser.add_argument('-l', '--limit-first', action='store_true', dest='lim_first',
                        help='Flag to limit who goes first or second in new cycle')

    return parser.parse_args()

#####################################

def _get_list_items_from_stdin():
    """ Read in list to shuffle from standard input
    """
    list_items = list()
    print("Enter a blank line to denote end of the list!")
    while True:
        list_items.append(input("Participant name: "))
        if list_items[-1] == '':
            print("----")
            return list_items[:-1]

#####################################

if __name__ == '__main__':
    """ Main script to do the shuffling
    """
    # 1) Read command line arguments
    args = _parse_args()

    # 2) Set up seeding for random number generator used to shuffle names
    NOW = time.time()
    SEED = int(NOW) % 10000
    print(f'time.time() = {NOW} so seeding with {SEED}\n----')
    random.seed(SEED)

    # 3) If previous cycle was written to a file, read it back in
    #    We store use_previous_cycle_file because it determines if there are restrictions
    #    to the order of the shuffling (e.g. last person can't subsequently go first)
    previous_cycle_file = 'previous_cycle.txt'
    use_previous_cycle_file = os.path.isfile(previous_cycle_file) and not args.cmd_line
    if use_previous_cycle_file:
        previous_cycle = open(previous_cycle_file, "r")
        orig_people = previous_cycle.read().splitlines()
        previous_cycle.close()
    else:
        orig_people = _get_list_items_from_stdin()

    # 4) Do the shuffling and print results
    people = orig_people.copy()
    random.shuffle(people)
    if use_previous_cycle_file and args.lim_first:
        # If we read in the last cycle from a file, we want to
        # limit who can go first or second in the new cycle
        while (orig_people[-1] in people[:2]) or (orig_people[-2] == people[0]):
            print(f'Reshuffling, {people} is not valid order')
            random.shuffle(people)
    print(f'\nOriginal list\n{orig_people}')
    print(f'\nShuffled list\n{people}')

    # 5) Store cycle in new file
    previous_cycle = open(previous_cycle_file, "w+")
    for person in people:
        previous_cycle.write(f'{person}\n')
