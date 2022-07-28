# Multiply all elements in a string
# Option-1
l = [2,3,4,5,'a','s','k','e','g']
lst = []
factor = 2
for i in range(len(l)):
    lst.append(factor*l[i])
    #l[i] *= factor # Modifying the list
print(lst)
#print(l)

# Option-2
my_list = [3,5,7,9]
factor = 2
for i, element in enumerate(my_list):
    my_list[i] = element * factor # Modify the list
print(my_list)
# enumurate(my_list)  returns.....>  [(0,3),(1,5),(2,7),(3,9)] index of the element & element