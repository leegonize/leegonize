tuition = 8000
percentincrease = .03

tuition += tuition * percentincrease
print(f'In 1 year, the tuition will be ${tuition:.2f}.')

for num in range (2,6):
    tuition += tuition * percentincrease
    print(f'In {num} years, the tuition will be ${tuition:.2f}.')