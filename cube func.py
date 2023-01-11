#using simple funcation
def cube(y):
  return y*y*y
n = int(input("please enter your number: "))
print(cube(n))

# using lambda func
n = int(input("Please enter your number: "))
f = lambda x: x*x*x
print(f(n))