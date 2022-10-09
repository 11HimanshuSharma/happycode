#slicing of strings
my_text = 'Python Programing'

# get slice object to slice Python
final_text = slice(6)
print(my_text[final_text])

# Output: Python

text = 'bat ball'

#Replacing

# replace b with c
replaced_text = text.replace('b', 'c')
print(replaced_text)

# Output: cat call


#concatenating strings

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)

#indexing
word = "hello, welcome to my world"
x = word.index("welcome")
print(x)

#output 7


#boolean expression

print(bool('hello everyone'))
#output true

print(bool(20))
#output true

print(bool(['himanshu', 'sharma']))
#output true



print(bool(""))
print(bool())
print(bool([]))
print(bool({}))

# output all of these false



#python lists
# lists are used to store multiple items of either same or different types into
#a singlevarible and are created using square brackets


my_list = [10, 30, 'Himanshu', 'sharma']
print(my_list)

#output 10, 30, Himanshu, sharma

#we can do these things with the lists
#oredered collectin - items are in defined order
#changeable - add, remove items
#allow duplicates


my_list = [20, 30, 40, 'apple',]
print(my_list[2])

#output 30


my_list = [12,4900, 8289, 'hello', 'hi']
print(my_list)


#outut 12,4900,8289, hello,hi


#add items in list

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#output ['apple', 'banan','cherry','orange']

#remove items from lists

# create a list
my_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
my_numbers.remove(9)


# Updated prime_numbers List
print(my_numbers)

# Output:  [2, 3, 5, 7, 11]
