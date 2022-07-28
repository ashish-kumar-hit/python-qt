# Check if the string is palindrome
def palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
s = input("Enter Word: ")
print(palindrome(s))