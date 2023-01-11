def compute_Hcf(x, y):
  while(y):
    x, y = y, x%y
  return x

hcf = compute_Hcf(300, 400)
print("The hcf is", hcf)