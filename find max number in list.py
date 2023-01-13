#creating empty list

list = []

#user enters the numbers of elements
num = int(input("How many elements do you want in your list:  "))


#Iterating till num to append

for i in range(num):
  l = int(input("Please enter numbers: "))
  list.append(l)



print("Largest element of the list is :", max(list))