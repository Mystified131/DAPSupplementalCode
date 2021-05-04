#Here is a solution to the Strings Code Challenge

#Here is our function
def Test_If_Substring(a, b):
    a1 = str(a)
    b1 = str(b)
    if a1 in b1:
        rstr = "True"
    if a1 not in b1:
        rstr = "False"
    return rstr

#Here is the main body
#Here we create a string, assigning it to a variable
astr = "Hello my name is Thomas."
#Let's take an input
bstr = input("Please enter a series of characters and press 'return': ")
#And we will call the function
ans = Test_If_Substring(bstr, astr)
print("Is the entered string a substring of the secret string?: ", ans)
