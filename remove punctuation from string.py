punctuations = "!()-[];:'\,<>./?@#$%^&*_~"

my_str = input("Please enter any string which have special characters.")

#to take input from the user
no_punct = ""
for char in my_str:
  if chr not in punctuations:
    no_punct = no_punct + char

print(no_punct)