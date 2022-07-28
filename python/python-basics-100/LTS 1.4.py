# Print the elements at their indexes
# Option-1
my_list = [2,4,5,6,7,8,9]
for index,element in enumerate(my_list):
    print(index,element,end = '\n')
print('\n')
# option-2
if not my_list:
    print("Empty List")
else:
    for i in range(len(my_list)):
        print(i,my_list[i])