# Count number of vowels in a string
def count_vowels(s):
    if not s:
        return 0
    elif s[0] in ['a','e','i','o','u']:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
s = input("Enter String: ")
s = s.lower()
l = ['a','e','i','o','u']
print(count_vowels(s))
