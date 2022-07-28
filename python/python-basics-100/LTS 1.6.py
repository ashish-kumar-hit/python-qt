# Remove the duplicates from the list
# Option-1
my_list = [1,23,1,4,5,3,4]
print(set(my_list))
# Option-2
no_duplicates = list(dict.fromkeys(my_list)) # Order will be preserved
print(no_duplicates)