# Check aLl values are equal
my_dict = {}
unique_values = len(set(my_dict.values()))
if unique_values == 0:
    print("Empty")
elif unique_values == 1:
    print(True)
else:
    print(False)
