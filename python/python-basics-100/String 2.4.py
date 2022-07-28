# Check the string if ends with a Suffix
# Option-1
s = input('Enter String: ')
suffix = input('Enter String: ')
print(s[1:] == suffix)

# Option-2
print(s.endswith(suffix))