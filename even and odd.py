num = int(input("Please enter your number: "))

flag = num%2
if flag == 0:
  print(num, "is an even number")
elif flag == 1:
  print(num, "is an odd number")
else:
  print("Error, Invalid input")