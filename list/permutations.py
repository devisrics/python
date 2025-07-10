from itertools import permutations
my_list=[1,2,3]

elem=list(permutations(my_list))       #permutations returns tuples

for val in elem:
    print(val)

