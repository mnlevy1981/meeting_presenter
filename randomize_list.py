#!/usr/bin/env python

"""
    This script shuffles a list; helpful for organizing a series of talks or picking folks
    to run a meeting without needing to ask for volunteers or draw names out of a hat.
"""

import os
import random
import time
import sys

#####################################

def _parse_args():
    """ Parse command line arguments
    """
    import argparse

    parser = argparse.ArgumentParser(description="Shuffle elements of a list",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--output-file', action='store', dest='output_file',
                        default='previous_list.txt',
                        help='File where the shuffled list where be saved')

    parser.add_argument('-n', '--new-list', action='store_true', dest='new_list',
                        help='Flag to force user to enter new list from command line')

    parser.add_argument('-l', '--limit-first', action='store_true', dest='lim_first',
                        help='Flag to limit who goes first or second in next shuffling')

    parser.add_argument('--clean', action='store_true', dest='clean',
                        help='Delete existing output file')

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
    if args.clean:
        if os.path.isfile(args.output_file):
            os.remove(args.output_file)
        sys.exit(0)

    # 2) Set up seeding for random number generator used to shuffle names
    NOW = time.time()
    SEED = int(1000*NOW) % 10000
    print(f'time.time() = {NOW} so seeding with {SEED}\n----')
    random.seed(SEED)

    # 3) If previous results were written to a file, read them back in
    #    We store use_previous_list_file because it determines if there are restrictions
    #    to the order of the shuffling (e.g. last person can't subsequently go first)
    previous_list_file = args.output_file
    use_previous_list_file = os.path.isfile(previous_list_file) and not args.new_list
    if use_previous_list_file:
        previous_list = open(previous_list_file, "r")
        orig_people = previous_list.read().splitlines()
        previous_list.close()
    else:
        orig_people = _get_list_items_from_stdin()

    # 4) Do the shuffling and print results
    people = orig_people.copy()
    random.shuffle(people)
    if use_previous_list_file and args.lim_first:
        # If we read in the previous results from a file, we may want
        # to limit who can go first or second in the next shuffling
        while (orig_people[-1] in people[:2]) or (orig_people[-2] == people[0]):
            print(f'Reshuffling, {people} is not valid order')
            random.shuffle(people)
    print(f'\nOriginal list\n{orig_people}')
    print(f'\nShuffled list\n{people}')

    # 5) Store new order in new file
    previous_list = open(previous_list_file, "w+")
    for person in people:
        previous_list.write(f'{person}\n')
