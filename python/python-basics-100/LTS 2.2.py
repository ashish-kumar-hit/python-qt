# Print Common elements in two lists
l1 = [1,2,3,4]
l2 = [1,2,3]
common = []
for elem in l1:
    if elem in l2:
        common.append(elem)
print(common)