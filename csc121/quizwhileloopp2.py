total = int()
numOfGrades = int()
grade = str()
average = float()

grade = input()

while grade != "stop":
    numOfGrades = numOfGrades + 1
    total = total + int(grade)
    average = total/numOfGrades
    grade = input()
print (average)