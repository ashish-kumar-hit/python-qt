# Replace A Character
# Logic-1
s = input("Enter String: ")
new_string = ''
curr_char = input('Enter curr_char: ')
new_char = input("Enter new_char: ")
for char in s:
    if char == curr_char:
        new_string += new_char
    else:
        new_string += char
print(new_string)

# Logic-2
s = input("Enter String: ")
curr_char = input('Enter curr_char: ')
new_char = input("Enter new_char: ")
print(s.replace(curr_char,new_char))
