#Function to reverse a sting

def reverse(string):
  # we know that about[start:end:step] and [::end] and [start::]
  #for reversing a string
  string = string[::-1]
  return string


#Driver Program to test above functions
string = input("Please any string that you want to reverse: ")
string = reverse(string)
print("The reverse string will be:", string)