# Check Number is Prime or Not
print("Enter Number")
num = int(input())
count = 0
if num == 1:
    print("Non-Prime")
else:
    for i in range(2,num + 1):
        if num % i == 0:
            count += 1
        else:
            pass
    if count == 1:
        print("Prime Number")
    else:
        print('Non-Prime')