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

lsta = [ 1, 2, 3]
lstb = ["red", "blue", "yellow"]

dictb = {}

for x in range(3):
    dictb[lsta[x]] = lstb[x]
print(dictb)

#Create a dictionary using loops

lsta = [ 1, 2, 3]
lstb = ["red", "blue", "yellow"]

dictb = {}

for x in range(3):
    dictb[lsta[x]] = lstb[x]
print(dictb)

#Import a .txt file. Iteratate through the data, creating a list of all strings that start with "S". Print the list.

infile = open("BillOfRights.txt", "r")

content = []

plist = infile.readline()
while plist:
    alist = plist.split()
    for elem in alist:
        if elem[0] == "s":
            content.append(elem)
    plist = infile.readline()

infile.close()

print(content)

#Use 3 inputs, send the strings to a function, have the function return a list of the inputs

def make_list_b(a, b, c):
    alst = []
    alst.append(a)
    alst.append(b)
    alst.append(c)
    return alst

a = input("Please enter one string, and press return: ")
b = input("Please enter a second string, and press return: ")
c = input("Please enter another string, and press return: ")

g = make_list_b(a, b, c)

print(g)

#Create a code that has 2 functions. Have one call the other as part of the code.

def to_lowercase(a):
    b = a.lower()
    return b

def make_list_c(a, b, c):
    alst = []
    alst.append(to_lowercase(a))
    alst.append(to_lowercase(b))
    alst.append(to_lowercase(c))
    return alst

d = make_list_c("Help", "Me", "Rhonda")
print(d)


