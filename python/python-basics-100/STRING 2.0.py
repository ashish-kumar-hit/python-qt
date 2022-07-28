# Replace Comma with Dot
# Option-1
s = input('Enter String: ')
comma = ','
dot = '.'
new_s = ''
for char in s:
    if char == ',':
        new_s += dot
    else:
        new_s += char
print(new_s)

# Option-2
s = input('Enter String:  ')
comma = ','
dot = '.'
print(s.replace(',','.'))