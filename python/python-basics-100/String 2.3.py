# Check the string Starts with Prefix
s = input('Enter String: ')
prefix_s = input("Enter Prefix String: ")
result = False
while len(s) > len(prefix_s):
    if prefix_s in s:
        result = True
        break
    else:
        break
print(result)

# Option-2
s = input('Enter String: ')
prefix_s = input("Enter Prefix String: ")
print(s[:len(prefix_s)] == prefix_s)

# Option-3
print(s.startswith(prefix_s))