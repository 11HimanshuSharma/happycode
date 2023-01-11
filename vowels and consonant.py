#program to check that given ch is vowels or consonant

ch = input("Please enter your char:")
vowels = "aeiouAEIOU"

if ch in vowels:
  print("The given char is a vowel")
else:
  print("The given char is not a vowels. it is a consonant")
