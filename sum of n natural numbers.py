# this program is for submission of n natural numbers

num = int(input("Please enter any number: "))


sum = 0
hold = num

if num<=0:
  print("Please enter a positive value")
else:
  while num>0:
    sum = sum + num
    num = num-1

print("The sum of n natural number will be:", sum)