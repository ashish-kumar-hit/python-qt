# Find maximum value in the dict
my_dict = {}
if my_dict:
    max_value = max(set(my_dict.values()))
    print(max_value)
else:
    print(None)