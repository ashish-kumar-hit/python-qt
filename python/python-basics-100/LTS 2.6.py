# Flatten a List that contains Lists
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [1,2,3,4,5,6,[7,8,9]]
l3 = [['a','b','c'],['d','e','f'],['g','h','i']]
l =[]
for i in range(len(l3)):
    if type(l3[i]) == int:
        l.append(l3[i])
    else:
        for j in range(len(l3[i])):
            l.append(l3[i][j])
print(l)

# Option-2
for elem in l1:
    if isinstance(elem,list):
        for nested_list in elem:
            l.append(nested_list)
    else:
        l.append(elem)
print(l)