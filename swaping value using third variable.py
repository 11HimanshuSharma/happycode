# program to swap two varibles
num1 = input("Enter first Number: ")
num2 = input("Enter second Number: ")

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

#swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp


print("The value of num1 after swapping: ", num1)
print("The value of num2 after swapping: ", num2)
