#creating Multiplicaton table using loops
num = int(input("Please Enter your number: "))

for i in range(num):
  print("Multiplication table of",i)

  for j in range(1,11):
    print(f"{i} X {j} = {i*j}")



#multiplication table using OOPS

class cump:

  def __init__(self, num):
    self.num = num

  def tab(self):
    for i in range(num):
      print("\n\nMultiplication table for {}\n".format(i))

      for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

obj = cump(num)
obj.tab()