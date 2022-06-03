primarycolor1 = input('Enter primary color:')
primarycolor2 = input('Enter primary color:')

if primarycolor1 == 'red' and primarycolor2 == 'blue':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get purple.')
elif primarycolor1 == 'blue' and primarycolor2 == 'red':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get purple.')
elif primarycolor1 == 'red' and primarycolor2 == 'yellow':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get orange.')
elif primarycolor1 == 'yellow' and primarycolor2 == 'red':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get orange.')
elif primarycolor1 == 'blue' and primarycolor2 == 'yellow':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get green.')
elif primarycolor1 == 'yellow' and primarycolor2 == 'blue':
    print('When you mix',primarycolor1,'and',primarycolor2,'you get green.')
else:
    print('You didn\'t input two primary colors.')