#variables
totalbugs = 0
#for loop to total each day
for num in range (1, 6):
    bugs = int(input("Enter number of bugs collected: "))
    totalbugs = totalbugs + bugs
print(totalbugs)