# Find the number of dates between two Dates
import datetime
date_1 = input('Enter first date in the format (YYYY MM DD): ')
date_2 = input('Enter second date in format (YYYY MM DD): ')

date_1_list = date_1.split(' ')
date_2_list = date_2.split(" ")
year1 = int(date_1_list[0])
month1 = int(date_1_list[1])
day1 = int(date_1_list[2])
year2 = int(date_2_list[0])
month2 = int(date_2_list[1])
day2 = int(date_2_list[2])

date1_obj = datetime.date(year1,month1,day1)
date2_obj = datetime.date(year2,month2,day2)

if date2_obj < date1_obj:
    print("Please enter valid input")
else:
    difference = (date2_obj - date1_obj).days

    if difference == 0:
        print("These dates are equal")
    else:
        print(f'There is {difference} between these two dates')