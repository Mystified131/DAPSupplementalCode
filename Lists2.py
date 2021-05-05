#Here I set up the three lists
alst = [1, 5, 6, 8, 7, 6, 3]
blst = ["bear", "cat", "shark"]
clst = [1.2, 3.6, 3.42]

#Here I create a new list
finlst = []

#Here I loop through each list, adding the elements to the new list
for elem in alst:
    finlst.append(elem)

for  elem2 in blst:
    finlst.append(elem2)

for elem3 in clst:
    finlst.append(elem3)

#Here I print the contents of the new list
print(finlst)