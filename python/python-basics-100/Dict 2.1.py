# Make a dictionary from Nested List
# Option-1
my_list = [['a',1],['b',2],['c',3],['d',4]]
my_dict ={}
for i in range(len(my_list)):
    for j in range(len(my_list[i])-1):
        my_dict[my_list[i][j]] = my_list[i][j+1]
print(my_dict)

# Option-2
for nested_list in my_list:
    key = nested_list[0]
    value = nested_list[1]
    my_dict[key] = value
print(my_dict)