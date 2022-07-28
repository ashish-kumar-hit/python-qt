# Print maximum sum of values in the dictionary
# Option-1
my_dict = {'a':[1,2,3],'b':[4,0,-4],'c':[3,5,9],'d':[45,12,100]}
my_list =[]
for nested_list in my_dict.values():
    my_list.append(sum(nested_list))
print(max(my_list))

# Option-2
max_sum = None
for nested_list in my_dict.values():
    list_sum = sum(nested_list)
    if max_sum is None:
        max_sum = list_sum
    elif list_sum > max_sum:
        max_sum = list_sum
print(max_sum)