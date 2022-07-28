# Given a phrase, determine whether or not it is a palindrome.
# Symbols, punctuation, and special characters should be ignored.

string = "Hey! What's 689458 up bro?"      # User Input
# Remove all un-necessary characters & join them.
new_string = ''.join(char for char in string if char.isdigit())  # 689458
# Here char is a variable. By using for loop we can iterate each character in the string one by one.
# With the help of Flow control we will check the character is digit or not. If yes then concatenate it into new_string
if new_string[::] == new_string[::-1]:  # 698458 == 854896 ..> returns False
    print('Palindrome Number')

else:
    print('Not Palindrome Number')