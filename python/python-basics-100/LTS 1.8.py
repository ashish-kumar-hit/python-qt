# Count element greater than 3
my_list = [1,5,7,8.9,4,2]
a = 0
for i in range(len(my_list)): # for element in my_list:
    if my_list[i] > 3:        #       if element > 3:
        a+=1
print(a)
# Option-2
count = sum(1 for element in my_list if element > 3)
print(count)