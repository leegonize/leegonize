numofweekday = int(input('Enter a number 1 through 7: '))

if numofweekday < 1 or numofweekday > 7:
    print('Please enter a number through 1 and 7.')
elif numofweekday == 1:
    print('Monday')
elif numofweekday == 2:
    print('Tuesday')
elif numofweekday == 3:
    print('Wednesday')
elif numofweekday == 4:
    print('Thursday')
elif numofweekday == 5:
    print('Friday')
elif numofweekday == 6:
    print('Saturday')
else:
    print('Sunday')