"""
Generate pseudo-random sequences of letters A, B, C, and D to randomize the
trials for each block. This way, you ensure category A will follow, e.g.,
category B as many times as, e.g., category D follows category A (and the
same for the rest of the combinations).
"""

from itertools import permutations
import random

perms = [''.join(p) for p in permutations('ABCD')]
random.shuffle(perms)

print(perms)

############################################################

"""
Generate pseudo-random sequences of numbers from 1 to 9 to randomize the
presentation order of each stimulus within a category.
"""

random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9],  9)
