# this program is to find out largest among 3 numbers

num1 = int(input("please enter number 1 value: "))
num2 = int(input("please enter number 2 value: "))
num3 = int(input("please enter number 3 value: "))

if num1>=num2 and num1>=num3:
  lnum = num1
elif num2>=num1 and num2>=num3:
  lnum = num2
elif num3>=num1 and num3>=num2:
  lnum = num3
else:
  lnum = "Not defined"

print("The largest number among",num1,",",num2,",",num3,"is",lnum)