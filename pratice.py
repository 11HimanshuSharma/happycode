str = input("please write some thing ...")
str = str.casefold()
# casefold is strong method to convert string's all letters into smaller letter.
# it is similar to the lower()
vowels = "aeiou"
count = {}.fromkeys(vowels,0)
# fromkeys is to getting keys from string.

for i in str:
  if i in vowels:
    count[i] += 1

print(count)