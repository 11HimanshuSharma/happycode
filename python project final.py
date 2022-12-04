import math

class computation():
  
  def Tablemult(self, integer):
    self.integer = n
    
    for i in range(2, n +1):
      print("\n\nMULTIPLICATION TABLE OF {}: \n".format(i))
      for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
        
p = computation()
n = int(input())
p.Tablemult(n)