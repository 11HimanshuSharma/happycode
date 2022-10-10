# Doc strings - A docstring requires the text to be enclosed(suround) with triple- quotes

def add(a,b):
    #comment lines can be present before doc string.
    """Return the sum of goven arguments"""
    return a + b
print(add.__doc__)

def power(b,e):
    """return the power value.
    b -- is the base
    e -- is the exponent
    """
    return b ** e
print(power.__doc__)

# add() method is for oneline docstring
#power() method is for multiple docstring
#generally doc strings convert comments into output as a definition
# the python coding conventions specification recommends us to use triple quotes
# the main purpose of doc string in pytthon is to provide information on what a
# particular python obect does and not how it does