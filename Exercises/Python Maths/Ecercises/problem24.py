"""24. Write a Python program to generate all permutations of a list in Python."""

import itertools
def perm(lst):
    print(list(itertools.permutations(lst)))
    print(len(list(itertools.permutations(lst))))

perm([1, 2, 3, 4])
