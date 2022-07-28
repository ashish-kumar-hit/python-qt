# Check Vowels,Consonents & Digits
s = 'Score: 36'
vowel = ['a','e','i','o','u','A','E','I','O','U']
i = 0
while i < len(s):
    if s[i].isalpha():
        if s[i] not in vowel:
            print("{} is consonent".format(s[i]))
            i += 1
        else:
            print("{} is Vowel".format(s[i]))
            i+=1
    elif s[i].isdigit():
        print("{} is Number".format(s[i]))
        i+=1
    else:
        print("{} not a letter".format(s[i]))
        i+=1
