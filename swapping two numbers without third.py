#this program is to swap values without using other variable

num1 = input("Enter first Number: ")
num2 = input("Enter second Number: ")

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

#Swapping two numbers without using third var

num1, num2 = num2, num1

print("Value of num1 after swapping: ",num1)
print("Value of num2 after swapping: ", num2)
