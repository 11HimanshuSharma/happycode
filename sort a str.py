#this program is to sort alphabetically the Words
# from the string that provided by user
str = input("Please Enter any str that you want to sort: ")


# just slipt down any string into small characters.
#Now we know the words

words = str.split()

words.sort()
print("The Sorted words are : ", words)

for i in words:
  print(i)
