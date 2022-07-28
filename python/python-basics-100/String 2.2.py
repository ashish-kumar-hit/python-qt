# Remove Spaces from String
# Option-1
s = input("Enter String: ")
new_s = ''
for char in s:
    if char != ' ':
        new_s += char
print(new_s)

# Option-2
s = input('Enter String: ')
new_s = ''
print(s.replace(' ',''))
