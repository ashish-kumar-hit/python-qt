# Find Second largest value in list
# Option-1
l = [1,2,3]
l.sort()
if len(l) > 1:
    print(l[len(l)-2])
else:
    print(None)
# Option-2
if len(l) > 1:
    no_duplicates = set(l)
    no_duplicates.remove(max(no_duplicates))
    print(max(no_duplicates))
else:
    print(None)
