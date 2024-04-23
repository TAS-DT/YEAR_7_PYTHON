# filename: 01_output_variables.py

# 01 Output and Variables
# OUTPUT#######################################################################
# 1. printing text

print("Hello World!")

# errors

# mismatch quotation marks.
# print('hello World") # error SyntaxError: EOL while scanning string literal

# wrong function name
# write("Hello World!") # NameError: name 'write' is not defined

# no closing bracket
# print("Hello WOrld"  #SyntaxError: unexpected EOF while parsing

# 2. combining text

print("Harry" + "Potter")  # no space between
print("Harry " + "Potter")
print("Harry", "Potter")

# 3. printing numbers

print("13") # not a number - it is '1' '3' - strings - cannot do math
print(13) # this is a number - integer - can do math


# 4. printing quotation marks

# print("He said "Hi"") #SyntaxError: invalid syntax
print('He said "Hi"')
print("Don't")

# VARIABLES ##################################################################

# 1. create a variable
name = "Mr Roberts"  # creates a label to point to the data "Mr Roberts"
my_name = "Mr Roberts"
myName = "Mr Roberts"

# 7A is using snake_case for variable names.
# lower case, no spaces, no special characters. use _ instead of space.
capital_of_australia = "Canberra"
name_of_pet = "Snoopy"

# 2. create a string variable
fav_food = "Baked Bean Milkshake"
fav_my_little_pony = "Stinky Pie"
second_fav_my_little_pony = "Scootaloo"

# 3. create a numeric variable
my_age = 103  # integer - how old i feel.
iphone_width = 7.8 # float  5.2324234 1.3 3.14159

# 4. create a boolean variable
is_it_raining = True # capital T
need_hat = False # capital F




# OUTPUT VARIABLES ############################################################

# 1. Print a string
print("Mr Roberts")
print(name)

print("1: Hello", name)
print("2: Hello " + name)

print(f"3: Hello {name}")  # when using variables use print(f"") - format vars
print(f"Hello {name} you are {my_age} years old.")  
print(f"Your iphone is {iphone_width} cm wide.")
print() # prints a blank line
print(f"\tLook at this.\nThis is on a new line!\n{name}") # \t tab \n new line

# 2. Print a number
temp_in_c = 23.5
pots_of_honey = 4
hours_of_chores = 2
hours_homework_done = 3

# error 
#print("It is " + temp_in_c + "c today") #TypeError: can only concatenate str (not "float") to str

print("It is " + str(temp_in_c) + "c today")

print(f"It is {temp_in_c}c today")
# if i forget the f
print("It is {temp_in_c}c today")


# 3. print the result of a calculation


# 4. combine a some text and a string


# 5. combine text and a number


# 6. output mulitple lines of text.


# more information.
#  
#  https://tascairns.sharepoint.com/sites/LearningPython/SitePages/Python-01-.aspx
#  