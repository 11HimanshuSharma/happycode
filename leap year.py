year = int(input("Please enter your leap year:"))
# simple method

if year%4==0:
  if year%100==0:
    if year%400==0:
      print("{0} is a leap year".format(year))
    else:
      print("{0} is not a leap year".format(year))
  else:
    print("{0} is not a leap year".format(year))
else:
  print("{0} is not a leap year".format(year))


#shorthand method
year = int(input("please enter your number:"))
if (year%4==0 and year%100==0 and year%400):
  print("{} is a leap year".format(year))
else:
  print("{} is not a leap year".format(year))