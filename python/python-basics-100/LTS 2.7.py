# Genearte all Permutations of the list
import itertools
my_list = [1,2,3]
permutations = list(itertools.permutations(my_list))
for permutation in permutations:
    print(list(permutation))