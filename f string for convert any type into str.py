# dont change the code below
age = input("what is your current age")
# dont chanege the code above

remaing_age = 90 - int(age)
days = int(remaing_age)*365
weeks = int(remaing_age)*365
weeks /= 7
months = int(remaing_age)*12


print(f"you have {days} days, {weeks} weeks, and {months} months")