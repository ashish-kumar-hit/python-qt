# Find Number of a days in a month
month = input('Enter Month : ')
month_31_days = ('Jan','Mar', 'May','July','Aug','Oct','Dec')
month_30_days = ('April','June','Sep','Nov')
if month in month_31_days:
    print("Month of 31 Days")
elif month in month_30_days:
    print("Month of 30 Days")
else:
    print('Month of 28 Days')
