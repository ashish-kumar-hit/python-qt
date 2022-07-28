# Reverse a String using loops
#Option-1
s = "Python"
for i in range(len(s)-1, -1,-1): # reversed(len(s)):
    print(s[i],end = '')
print('\n')

# Option-2
for char in s[::-1]: #reversed(s):
    print(char,end='')