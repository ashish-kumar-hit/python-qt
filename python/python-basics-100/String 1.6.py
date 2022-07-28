# Remove nth Character from the String
# Logic-2
s = input("Enter a String: ")
i = int(input("Enter number want to remove from string: "))
new_string = ''
if len(s) == 0 or i >= len(s): # if (not s) or i >= len(s):
    print(s)
else:
    for j in range(len(s)):
        if j != i:
            new_string += s[j]
        else:
            pass
print(new_string)


