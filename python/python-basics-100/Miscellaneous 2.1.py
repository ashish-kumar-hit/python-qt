# Print a Calender
import calendar
print("Welcome to Your Python calendar")

year = int(input("Enter year in the format YYYY: "))
month = int(input("Enter month in between (1-12): "))
print(calendar.month(year,month))