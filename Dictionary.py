#A dictionary is created using curvy brackets
adict = {}

#You can add values when you create a dictionary
bdict = {"one": "red", "two": "blue", "three": "yellow"}

#If you print a dictionary, you will see its key:value pairs
print(bdict)

#You can call a value by it's key
print(bdict["one"])
print(bdict["three"])

#You can create a dictionary using a loop or other data process
cdict = {}

for x in range(10):

    cdict[x] = x * 10

print(cdict)

#You can split a dictionary into lists of keys and values

bk = bdict.keys()
bv = bdict.values()

print(bk)

print(bv)