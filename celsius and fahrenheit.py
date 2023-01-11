# program to convert celsius to fahrenheit
celsius = float(input("Enter temp in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("%.2f celsius is: %0.2f Fahrenheit"%(celsius, fahrenheit))


#program to convert fahrenheit to celsius
fahrenheit = float(input("Enter temp in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("%.2f Fahrenheit is: %0.2f celsius"% (fahrenheit, celsius))