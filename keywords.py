# keyword - every programming usally has a set of words known as keywords
# they reserved for special meaning and purpose. they are used only for intended
# purpose
# we cannot use keyword as a variable name, funcation name or any other
# indentifier name.

# pyhton also has reserved words called keywords
#python has total 35 keywords

import keyword # this statement is used to import keyword module
print(keyword.kwlist) # all keywords of python

#output
#False		class		finally		is			return
#None		continue	for			lamda		try
#rue		def			from		nonlocal	while
#and			del			global		not			with
#as			elif		if			or			yield
#assert 		else		import	 	pass
#break		except		in			raise

#to wheather a given word is a pyhon keyword or not, we use a built in funcation
# iskeyword.
#this funcation as a boolean value.

import keyword
list = ["apple", "finally", "global"]

if keyword.iskeyword(list[0]):
    print("apple : true")
else:
    print("apple : false")

if keyword.iskeyword(list[2]):
    print("global : true")
else:
    print("global : false")