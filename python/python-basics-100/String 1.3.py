# First & Last 3 Character of a String
# Logic-1
s = input("Enter String: ")
l = []
if len(s) < 6:
    print("''")
else:
    for i in range(3):
        l.append(s[i])
    for i in range(len(s)-3, len(s)):
        l.append(s[i])
    print(''.join(l))

# Logic-2

s = input("Enter String for Second Way: ")
if len(s) < 6:
    print('""')
else:
    new_string = s[:3] + s [len(s) - 3 :] # Concatenation
    print(new_string)
