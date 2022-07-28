# Find intersection of two sets
# Option-1
set1 = {2,3,5,9,12}
set2 = {4,7,2,12,9}
set3 = {2,12,8,3,1}
intersection = set()
for elem in set1:
    if elem in set2:
        intersection.add(elem)
print(intersection)
# Option-2
print(set1.intersection(set2))
# Multiple Sets
print(set1.intersection(set2,set3))