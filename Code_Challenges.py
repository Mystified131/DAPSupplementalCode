#Create a string, a list, a dictionary
#1. Declare the data manually
#2. Use a loop to declare the data

astr = "This is a string."
alst = ["this", "is", "a", "list"]
adict = { 1 : "red", 2 : "blue", 3 : "yellow"}

lsta = [ 1, 2, 3]
lstb = ["red", "blue", "yellow"]

dictb = {}

for x in range(3):
    dictb[lsta[x]] = lstb[x]
print(dictb)


#Create a function that turns 3 strings into a list

def Make_List( a, b, c):
    alst = []
    alst.append(a)
    alst.append(b)
    alst.append(c)
    return alst

ast = "one"
bstr = "two"
cstr = "three"
clst = Make_List(ast, bstr, cstr)

print(clst)


#Create a dictionary from 2 lists

#Create a dictionary using loops

#Import a .txt file. Iteratate through the data, creating a list of all strings that start with "S". Print the list.

#Use 3 inputs, send the strings to a function, have the function return a list of the inputs

#Create a code that has 2 functions. Have one call the other as part of the code.


