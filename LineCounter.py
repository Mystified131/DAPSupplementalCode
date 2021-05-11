infile = open("CollectedGenJams.m3u", "r")
   
content = []

plist = infile.readline()
while plist:
    content.append(plist)
    plist = infile.readline()

infile.close()

l = len(content)

print("")

print("The number of lines in this file are: ", l)

print("")