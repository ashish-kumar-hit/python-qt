# Balanced Square Bracket
n = input("Enter Brackets: ")
count = 0
for i in range(len(n)):
    if n[i] == '[':
        count += 1
    else:
        count -= 1
    if count < 0:
        break
if count == 0:
    print('Balanced')
else:
    print('Not-Balanced')

