n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1<=n2 and n1<=n3:
  snum = n1
elif n2<=n1 and n2<=n3:
  snum = n2
else:
  snum = n3

print(f"the smallest number in between {n1}, {n2}, {n3} is {snum}")