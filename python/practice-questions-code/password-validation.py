# New challenge: Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according
# to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

l = input().split(',')
import re
for i in range(len(l)):
    if 6 <= len(l[i]) <= 12:
        if re.search('[a-z]',l[i]):
            if re.search('[A-z]',l[i]):
                if re.search('[$#@]',l[i]):
                    if re.search('[0-9]',l[i]):
                        print(l[i])

# Explanation

# Step1: Take User Input,Store them as a list
# Step2: Import regular expression module to Check Criteria of the Password
# Step3: Using for loop Check all the Criteria one after another & print the result
