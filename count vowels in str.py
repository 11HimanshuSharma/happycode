#just count the vowels
str = input("please write something here.........")

vowels = "aeiouAEIOU"

count = 0
for i in range(len(str)):
  if str[i] in vowels:
    count = count + 1
  else:
    pass
  

print(count)

# Program to count the number of each vowels
vowels = "aeiou"

ip_str = input("please write something ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
  if char in count:
    count[char] += 1
print(count)