# Find Second Smallest Value in the List
# Option-1
l = []
l.sort()
if len(l) > 1:
    print(l[1])
else:
    print(None)
# Option-2
if len(l) > 1:
    no_duplicate = set(l)
    no_duplicate.remove(min(no_duplicate))
    print(min(no_duplicate))