# Make a frequency dictionary for the characters in the string
my_string = "Python 123 #24$"
my_dict ={}
i =0
while i < len(my_string) -1:
    for item in my_string:
        if item.isalpha():
            my_dict[my_string[i]] = my_string.count(item)
            i += 1
        else:
            i += 1

print(my_dict)