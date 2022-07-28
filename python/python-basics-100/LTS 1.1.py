# Print elements on the same line
# Option-1
my_list = [3,4,5,6,'a','d']
for element in my_list:
    print(element, end = ' ')
print("\n")
# Option-2
print(*my_list, sep = ' ')