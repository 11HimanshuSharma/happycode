num = int(input("Please enter a number:"))

sum = 0


# we need to loop in while 
while num>0:
  rem = num%10
  sum = sum + rem
  num = int(num/10)

print("the sum will be: ")
print(sum)