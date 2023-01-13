#program to find min num in list

lis = []

#enter number how many elements do you want
num = int(input("Please Enter your numbers: "))

for i in range(num):
  itm = int(input("Please Enter list elements: "))
  lis.append(itm)


print("The minimum number in the list is: ", min(lis))
