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