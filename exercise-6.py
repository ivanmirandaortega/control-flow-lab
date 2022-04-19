# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year as three characters:')
day = int(input('Enter the day of the month:'))
season = ''

if (month == 'Dec' and day in range(21, 31)) or (month == 'Jan' and day in range(1, 31)) or (month == 'Feb' and day in range(1, 28)) or (month == 'Mar' and day in range(1, 19)):
    season = 'Winter'
elif (month == 'Mar' and day in range(20, 31)) or (month == 'Apr' and day in range(1, 30) or (month == 'May' and day in range(1, 31)) or (month == 'Jun' and day in range(1, 20))):
    season = 'Spring'
elif (month == 'Jun' and day in range(21, 30) or (month == 'Jul' and day in range(1, 31)) or (month == 'Aug' and day in range(1, 31)) or (month == 'Sep' and day in range(1, 21))):
    season = 'Summer'
elif (month == 'Sep' and day in range(22, 30) or (month == 'Oct' and day in range(1, 31)) or (month == 'Nov' and day in range(1, 30)) or (month == 'Dec' and day in range(1, 20))):
    season = 'Fall'

print(f'{month} {day} is in {season}')
