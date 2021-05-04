#Here we create a string, assigning it to a variable
astr = "Hello my name is Thomas."

#Printing the string
print(astr)

#Let's try looping through the string, printing each element. What happens?
for x in range(len(astr)):
    print(astr[x])

#Let's create a substring and see if it is "in" the longer string
bstr = "Thomas"
if bstr in astr:
    print("That is a substring.")
if bstr not in astr:
    print("That is not a substring.")

#Let's create a substring and see if it is "in" the longer string
cstr = "dre"
if cstr in astr:
    print("That is a substring.")
if cstr not in astr:
    print("That is not a substring.")

#Let's demonstrate slicing a string:
dstr = astr[3:5]
print(dstr)

estr = astr[:4]
print(estr)

fstr = astr[5:]
print(fstr)

#CODE CHALLENGE#

#Can you do this: Crate a program, with a function. The function will test if one string is a subset of another.
#It will return true or false.
#In the main body ask for input.
#Use the input to test the input string against the one you chose.
#Have the program print whether it is a substring or not.