posnum = int(input("Enter a nonnegative integer:"))
factorial = 1

if posnum < 0:
    print("Please enter a nonnegative integer.")

else:
  for num in range(1, int(posnum) + 1):
      factorial = factorial * num 
  print(factorial)


