# Check the pattern using Rugular Expression
import re
regex = "^My[\w\s]+blue$"
string = input("Enter a string to check the match if it found: ")

if re.search(regex,string):
    print("Match")
else:
    print("Not Match")