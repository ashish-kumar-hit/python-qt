# Difference between Two Lists
l1=[1,2,3,4]
l2=[1,2]
difference = []
for elem in l1:
    if elem not in l2:
        difference.append(elem)
print(difference)