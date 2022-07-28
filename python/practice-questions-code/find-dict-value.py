# Given a JSON file with several dictionaries in it, find the value for a given key.
# The key will always be in one of the dictionaries.
# Remember, post an explanation with your code.

# [{"Fruit": "Apples", "Lock": 4, "Code": "Python"},
# {"Market": "Bazaar", "Funny": true, "Math": 0.003, "Fly": false},
# {"Animal": "Aardvark", "7": "Lucky", "true": 1.6}]

import json
file_name = "05_names.json"
with open(file_name,'r') as f:
    data = f.read()
obj = json.loads(data)
print(obj)
index = int(input("Enter Index Number: "))
key = input('Enter Key : ')
print(str(obj[index][key]))

# Step1: Create .json files & Create json objects inside Array
# Step2: Create python file import json module
# Step3: Read json file & Parse it
# In Json files key is always str type hence we have to type cast during printing of values
