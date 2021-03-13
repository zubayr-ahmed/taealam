##############################################################################################
# Python getting started
##############################################################################################

i = 1
f = 2.2222
b = True
by = b"fe"
strs = "string"
print("Int {}, Float {}, bool {}, bytes {}, string {}".format(
    str(i), str(f), str(b), str(by), strs))

###############################################
# Basic strings
###############################################
my_string = "This is a string"
one_more_string = "This is another string"
long_string_multiline = """We can add multiple lines to a string
like we did here, we user the \"\"\" for this """  # we are using `\` to escape the `"`
print(my_string)  # >>> This is a string
print(long_string_multiline)  # >>> We can add multiple lines to a string
# like we did here, we user the """ for this
print("Let me put some string here")  # >>> Let me put some string here


###############################################
# String Concatenation
###############################################
my_string = "This" * 5
print(my_string)  # >>> ThisThisThisThisThis

###############################################
# Accessing by Index.
###############################################
strings1 = "This is a string, which we can access using index"
# string[<start>:<end>:step]
print(strings1)  # >>> This is a string, which we can access using index
print(strings1[::1])  # >>> This is a string, which we can access using index
print(strings1[0::1])  # >>> This is a string, which we can access using index
# >>> This is a string, which we can access using index
print(strings1[0:len(strings1):1])
# 10th char
print(strings1[10])  # >>> 5
# // 1 to 10 char including spaces [index starts at 0]
print(strings1[1:10])  # >>> his is a
# Last Char
print(strings1[-1])  # >>> x
# Char 10 to 1 in reverse
print(strings1[10:0:-1])  # >>> s a si sih
# Reversing a string is very simple now
print(strings1[::-1])  # >>> xedni gnisu ssecca nac ew hcihw ,gnirts a si sihT
# Start from the end of the string to the start.
# >>> xedni gnisu ssecca nac ew hcihw ,gnirts a si sihT
print(strings1[len(strings1)::-1])


###############################################
# String methods
###############################################
# String methods
string2 = "this is a SECOND string for methods."
print(string2.upper())  # >> THIS IS A SECOND STRING FOR METHODS.
print(string2.lower())  # >> this is a second string for methods.
print(string2.capitalize())  # >> This is a second string for methods.
# Create a Title for the string
print(string2.title())  # >> This Is A Second String For Methods.
# Converts string to list split over `space`
# >> ['this', 'is', 'a', 'SECOND', 'string', 'for', 'methods.']
print(string2.split())
print(len(string2))  # >> 32


###############################################
# Math Operations
###############################################

a = 2
b = 4
exp = a ** b
print("exp ", exp)  # >>> exp 16
add = a + b
print("add ", add)  # >>> add 6
sub = a - b
print("sub ", sub)  # >>> sub -2
mul = a * b
print("mul ", mul)  # >>> mul 8
int_div = 23 // a
print("int_div ", int_div)  # >>> int_div 11
div = 23 / a
print("div ", div)  # >>> div 11.5
mod = 23 % a
print("mod ", mod)  # >>> mod 1

###############################################
# Conversions
###############################################

# `int("15")`  string to int convertion 15
print(int("15"))

# `int("3f",16)`  63 can specify integer number base in 2nd parameter
print(int("3f", 16))

# `int(15.56)` float to int, 15 truncate decimal part
print(int(15.56))

# `float("-11.24e8")` string to float `-1124000000.0`
print(float("-11.24e8"))

# `round(15.56,1)`  `15.6` rounding to 1 decimal (0 decimal  integer number)
print(round(15.56, 1))

# `bool(x)` False for null `x`, empty container `x` , None or False `x` ; True for other `x`
x = 1
print(bool(x))

# `str(x)` representation string of `x` for display
print(str(x))

# `chr(64)` converts to charater '@'
chr(64)

# `ord('@')` 64 code char / `ord()` function returns the number representing the unicode code of a specified character
print(ord('@'))

# `repr(x)` literal representation string of `x`
# 	The `repr()` function returns a printable representation of the given object.
# 	Return a string containing a printable representation of an object.
# 	For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval, otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object.
# 	A class can control what this function returns for its instances by defining a `__repr__` method.
print(repr(x))

# `bytes([72,9,64])` converts to `b'H\t@'`
print(bytes([72, 9, 64]))

# `list("abc")` list convertion `['a','b','c']`
print(list("abc"))

# `dict([(3,"three"),(1,"one")])` converts to dictionary `{1:'one',3:'three'}`
print(dict([(3, "three"), (1, "one")]))

# `set(["one","two"])` convert to set  `{'one','two'}`
print(set(["one", "two"]))

# separator `str` and sequence of `str`  assembled `str`
# `':'.join(['toto','12','pswd'])` joins all strings in list with `:` delimiter,  `'toto:12:pswd'`.
print(':'.join(['toto', '12', 'pswd']))

# `str` splitted on whitespaces  `list` of `str`
# `"words with spaces".split()` split all words into list with space separator by default ['words','with','spaces']
# `"words,with,spaces".split(',')` split all words into list with `,` separater as passed on ['words','with','spaces']
print("words with spaces".split())
print("words,with,spaces".split(','))

# sequence of one type `list` of another type (via `list comprehension`)
# `[int(x) for x in ('1','29','-3')]`  convert from tuple to list [1,29,-3]
print([int(x) for x in ('1', '29', '-3')])

###############################################
# Built-in Functions
###############################################

print("Hello World")

# The input funciton allows you to prompt the user for a value
# You need to declare a variable to hold the value entered by the user
name = input('What is your name? ')
print("Welcome to Python {}!".format(name))

my_string = "This"
print(len(my_string))  # >>> 4


# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# Method


def filter_func(letter):
    if letter in ['a', 'i', 'c']:  # Compare `char` with contents of `list`
        return True  # boolean
    else:
        return False  # boolean


filtered_letters = filter(filter_func, letters)
for item in filtered_letters:  # looping over iterable object
    print(item)  # >>> a
# >>> i


###############################################
# Control Flow.
###############################################

# Since we have set the condition to `True`
# It will always go the first branch.
if True:
    print("I am always true")


input_age = input('What is your age? ')
age = int(input_age)
if age < 4:
    ticket_price = 0
    print("FREE!!")
elif age < 18:
    ticket_price = 10
    print("£10 per Ticket")
else:
    ticket_price = 15
    print("£15 per Ticket")

###############################################
# Comparators
###############################################


str1 = "One"
if str1 == "One":  # True
    print(True)  # >>> True
else:
    print(False)

###############################################
# Boolean Operations
###############################################

str1 = "One"
str2 = "Two"
str11 = "One"
if str1 == "One" and str11 == "One":  # True and True
    print(True)  # >>> True
else:
    print(False)
if str1 == "One" or str2 == "One":  # True or False
    print(True)  # >>> True
else:
    print(False)
if not str2 == "One":  # not False ==> True
    print(True)  # >>> True
else:
    print(False)


###############################################
# Accessing by Index for List .
###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits[<start>:<end>:step]
print(fruits)
print(fruits[::1])
print(fruits[0::1])
print(fruits[0:len(strings1):1])
print(fruits[4])
print(fruits[1:4])
print(fruits[-1])
print(fruits[4:0:-1])
print(fruits[::-1])
print(fruits[len(strings1)::-1])

#
# Conditional test with lists
#
motorcycles = ['yamaha', 'ducati', 'kawasaki', 'ktm']
# >>> This statement is `True` as the item is present in the list.
if 'ducati' in motorcycles:
    print("We have it in the list")
# >>> This statement is `True` (rather `!False`) as the item is not present in the list.
if 'indian' not in motorcycles:
    print("Sorry we dont.")

###############################################
# Operations on list
###############################################

# list.append(x) # Add an item to the end of the list.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('pineapple')
print(fruits)
# list.append(x) # Equivalent to a[len(a):] = [x].
fruits[len(fruits):] = ['pen-pineapple-apple-pen']
print(fruits)

###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.extend(['another-pineapple'])
print(fruits)
# Output
# >>> ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'another-pineapple']
###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.insert(0, 'another-pineapple')
print(fruits)
# Output
# >>> [ 'another-pineapple', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple']
fruits.insert(len(fruits), 'another-pineapple')
print(fruits)
# Output
# >>> [ 'another-pineapple', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'another-pineapple']
###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.remove('orange')
print(fruits)
# Output
# >>> [ 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple']
###############################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.pop(0)
print(fruits)
# Output
# >>> [ 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple']
fruits.pop()
print(fruits)
# Output
# >>> [ 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
###############################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.clear()
print(fruits)
# Output
# >>> []
###############################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('apple'))
# Output
# >>> 1
print(fruits.index('pear'))
# Output
# >>> 2
print(fruits.index('banana'))
# Output
# >>> 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
# Output
# >>> 3
###############################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# Output
# >>> 2
print(fruits.count('pear'))
# Output
# >>> 1
print(fruits.count('banana'))
# Output
# >>> 2
###############################################

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort()
print(fruits)
# Output
# >>> ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
print(fruits)
# Output
# >>> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

###############################################
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
new_fruits = fruits.copy()
print(new_fruits)
# Output

################################################
# Tuples
################################################

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4)  # Tuples may be nested:
print(u)
# Output
# >>> 12345
# >>> (12345, 54321, 'hello!')
# >>> ((12345, 54321, 'hello!'), (1, 2, 3, 4))


empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)
# output
# >>> 0
# >>> 1
# >>> ('hello',)

################################################
# Convert Tuple to a List
################################################
x = ("apple", "orange", "pear")
y = list(x)   # tuple to list Conversions
print(y)  # >>> ['apple', 'orange', 'pear']
x = tuple(y)  # list to tuple Conversions
print(x)  # >>> ("apple", "orange", "pear")


################################################
# Dictionaries
################################################

# Create a dictionary `countries` with keys of "CA", "GB", and "IN"
#   and corresponding values of of "Canada", "Great Britain", and "India"
countries = {"CA": "Canada", "GB": "Great Britain", "IN": "India"}
print(countries["GB"])  # >>> Great Britain
print(countries.get("AU", "Sorry"))  # >>> Sorry
print(countries.keys())  # >>> dict_keys(['CA', 'GB', 'IN'])
# >>> dict_items([('CA', 'Canada'), ('GB', 'Great Britain'), ('IN', 'India')])
print(countries.items())
# >>> dict_values(['Canada', 'Great Britain', 'India'])
print(countries.values())

################################################
# Looping Technique for Dictionaries
################################################
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)


################################################
#  Loops
################################################

list_a = ['a', 'b', 'c', 'd']
for item in list_a:
    print(item)

# output
# >>> a
# >>> b
# >>> c
# >>> d
###############################################
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1
###############################################
# output
# >>> 1
# >>> 2
# >>> 3
# >>> 4
# >>> 5

################################################
# Exception Handling
################################################

try:
    x = 1
except:
    print('Failed to set x')
else:
    print('No exception occured')
finally:
    print('We always do this')


################################################
# File Operation
################################################

# Open a file in write/update mode
# if the file is not present it will create one.
file_descriptor = open("foo.txt", "w+")
print("filename: ", file_descriptor.name)
file_descriptor.write("I am writting into this file")
# Close opend file
file_descriptor.close()


try:
    # Open a file in write/update mode
    # if the file is not present it will create one.
    file_descriptor = open("foo.txt", "w+")
    print("filename: ", file_descriptor.name)
    file_descriptor.write("I am writting into this file")
except:
    print("We have an exception")
finally:
    # Close opend file
    file_descriptor.close()

###############################################
# readline(size)
###############################################
try:
    with open("foo.txt", "r+") as file_descriptor:
        # get the first line.
        line = file_descriptor.readline(10)
        # Check if we have a line if so print it.
        while line:
            # Print the line
            print(line)
            # Move on to next line
            line = file_descriptor.readline(10)
except:
    print("We have an exception")
finally:
    # Close opend file
    file_descriptor.close()

# Output 10 char per line
#
# 1. I am wr
# itting int
# o this fil
# e
#
# 2. I am wr
# itting int
# o this fil
# e
#
# 3. I am wr
# itting int
# o this fil
# e
#
# 4. I am wr
# itting int
# o this fil
# e

###############################################
# file_descriptor.write()
###############################################
try:
    # Open a file in write/update mode
    # if the file is not present it will create one.
    file_descriptor = open("foo.txt", "w+")
    print("filename: ", file_descriptor.name)
    char_written = file_descriptor.write("I am writting into this file")
    print("We wrote {} chars to the file".format(char_written))
except:
    print("We have an exception")
finally:
    # Close opend file
    file_descriptor.close()

# Output
# We wrote 28 chars to the file
##############################################################################################
