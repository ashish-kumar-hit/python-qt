# Sort List in Ascending Order
# Option-1
my_dict = {'a':[2,3,1],'b': [3,7,5],'c':[10,1,9],'d':[1,3,4]}
my_list = []
new_dict = {}
i = 0
for value_list in my_dict.values():
    my_list.append(sorted(value_list))
while i < len(my_list) - 1:
    for item in my_dict.keys():
        new_dict[item] = my_list[i]
        i +=1
print(new_dict)

# Option-2
for sort_list in my_dict.values():
    sort_list.sort()
print(my_dict)