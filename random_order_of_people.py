#!/usr/bin/env python

"""
    Every meeting a different person from the BGC group will give a brief update on his or her work.
    Only exists so that we don't need to draw names out of a hat when the cycle is due to repeat.
"""

import random
import time

NOW = time.time()
SEED = int(NOW) % 10000
print(f'time.time() = {NOW} so seeding with {SEED}')
random.seed(SEED)

PEOPLE = ['Magdalena',
          'Kristen',
          'Mike',
          'Keith',
          'Matt',
          'Precious',
          'Dan'
         ]

print(f'\nOriginal list (group sorted alphabetically by last name, I hope)\n{PEOPLE}')
random.shuffle(PEOPLE)
print(f'\nShuffled list\n{PEOPLE}')
