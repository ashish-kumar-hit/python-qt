# Remove Characters from Even Indices
# Logic-1
s = input("Enter String: ")
if len(s) < 2:
    print(s)
else:
    print(s[1::2])

# Logic-2

s = input('Enter String: ')
new_string = ""
if len(s) < 2:
    print(s)
else:
    for i in range(len(s)):
        if i % 2 != 0:
            new_string += s[i] # Concatenation
    print(new_string)

#Logic-3

s = input('Enter String: ')
new_string = ""
for i in range(1,len(s),2):
    new_string += s[i]
print(new_string)
