# Check year is leap year or not
year = 1836
# Option-1
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# Option-2
if year % 400:
    print(f'{year} is a leap year')
elif year % 100:
    print(f'{year} is not a leap year')
elif year % 4:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# Option-3
if year % 4 != 0:
    print(f'{year} is not a leap year')
elif year % 100 != 0:
    print(f'{year} is a leap year')
elif year % 400 != 0:
    print(f'{year} is not a leap year')
else:
    print(f'{year} is a leap year')