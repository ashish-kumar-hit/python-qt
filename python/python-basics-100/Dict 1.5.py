# Find minimum value in the dictionary
my_dict = {'a':2,'b':3, 'c': 7, 'd': 2}
if my_dict:
    min_value = min(set(my_dict.values()))
    print(min_value)
else:
    print(None)