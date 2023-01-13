num = int(input("Please enter a number: "))
result = 0
hold = num

#while loop to iterate through all the digits of input numbers
while num>0:
  rem = num % 10
  result = result + rem
  num = int(num/10)

#displaying output
print("Sum of all digits of",hold, "is: ",result)

#n = input("Please enter any number: ")
#sum = 0
#for i in range(len(n)):
#  sum = sum + int(n[i])
#
#print(sum)