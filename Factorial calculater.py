#this program finds the factorial of anu numbers
#this program is finding factorial of any number using recursion

def factorial(num):
  if num == 1:
    return num
  else:
    return num*factorial(num-1)

num = int(input("Enter your number please: "))

if num<0:
  print("factorial is not defined for negative numbers")
elif num==0:
  print("The factorial of 0 is 1")
else:
  print(f"the factorial of {num} is {factorial(num)}")