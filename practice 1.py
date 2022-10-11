print("hello world")
print("hello how are you " + "I am fine")
print("hello\nI am Himanshu sharma")
print(len("Himanshu sharma"))
X = "Himanshu sharma"
print(len(X))
a = 20
b = 20.56
c = '20'
d = 'apple'

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a + b)
print(str(a) + str(b))
print(c + d)
print(a - b)


#print(len[1, 2, 3, 4,])
# type error object of type 'int' has no length


# we are going to study about some data types
# which are given below
#string
#float
#integer
#boolean - that gives output funcation as true and false

#type only one number from string
print("hello[0]")
e = "book"
print(e[3])

#you can't subtracte str with str

#input funcations
f = input("what is your age")
print(f)

num_char = len(f)
new_num_char = str(num_char)
print("your name has " + new_num_char + "characters")





# what is "PEMDAS"
#here p = perenthess ()
# E = exponents      **
# M = multiplication *
# D = division       /
# A = additions      +
# S = subtraction    -

# here that is PEMDAS rule. which is followed in mutliple math calculations

g = 9
h = 6
i = 8

print(g / h)
print(h / i)
print(i / g)
print(g*h)
print(h*i)
print(g**h)

# get round value after two decimal points
print(round(g / h, 3))
print(round(g / h))

# get int value by using '//'

print(9 // h)

score = 40
score += 50
print(score)


# f string - f string is a way to convert variables into str
# we can directly concorate strings by using F string

score1 = 90
height = 1.8
result1 = "true"
print(f"your name is {result1}, your score is {score}")
# other way
print("your name is " + str(score1) + " your score is " + str(result1) )


# turning letter cases
Z = " my name is Himanshu sharma"
print(Z.upper())
print(Z.lower())

#spliting strings
# how we split strings
W = Z.split()
print(W[3])
print(W[4])


# boolean expression

print(bool(["apple","dos"]))


#python lists

my_list = [1,2,3,4,5,6,7,8]
print(my_list)

# we can do thes thigs with the list
print(my_list[2])
