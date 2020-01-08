#!/usr/bin/env python

import random
import time


now = time.time()
seed = int(now) % 10000
print(f'time.time() = {now} so seeding with {seed}')
random.seed(seed)

people = ['Magdalena',
          'Kristen',
          'Mike',
          'Keith',
          'Matt',
          'Precious',
          'Dan'
         ]

random.shuffle(people)
print(people)
