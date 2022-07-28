# Remove matching element
# Option-1
my_list = [4,7,8,5,4]
element_remove = 4
a = -1
if not my_list:
    print("Empty List")
elif my_list.count(element_remove) == 0:
    print("Element not found")
else:
    while a < my_list.count(element_remove): # for i in range(my_list.count(element_remove))
        my_list.remove(element_remove)       #          my_list.remove(element_remove)
        a += 1
print(my_list)