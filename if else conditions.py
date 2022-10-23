#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      himan
#
# Created:     10-10-2022
# Copyright:   (c) himan 2022
# Licence:     <your licence>
#------------------------------------------------------------------------------

import keyword




list = ["except", "raise", "fall"]

if keyword.iskeyword(list[0]):
 print("except : true")
else:
 print("except : false")

if keyword.iskeyword(list[1]):
 print("raise : true")
else:
 print("raise : false")

if keyword.iskeyword(list[2]):
 print("fall : true")
else:
 print("fall : false")
 
 
 #multiple conditions in if else
 
 #using same result multiple conditions
 # question - find out leap year
 
y = int(input())
if ((y%400) or (y%4==0) and (y%100!=0)):
    print("is a leap year")
else:
    print("is not leap year")
    
    
#multiple conditons in if else with same conditions and different result
#quesetion

n = int(input())
if ((n%2!=0) or ((6<=n<=20) and (n%2==0))):
    print("Weird")
elif (((n%2==0) and (2<=n<=5)) or ((n%2==0) and (20<=n))):
    print("Not Weird")
else:
    print("Not Weird")