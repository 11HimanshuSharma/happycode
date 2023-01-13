num = int(input("Please enter how many elements you want: "))
lis = []
for i in range(num):
  a = int(input("Please enter elements: "))
  lis.append(a)

#now printing the list that you have made
print("The list we got:",lis)

# number of divisible by other number 
n = int(input("Please enter that's divisibilty you want to find: "))
result = list(filter(lambda x: (x%n==0),lis))


#so the final list will be
print("Numbers divisible by",n,"are",result)