file = open("file_newline_seek.txt", "r+")

# print (file.readline())
# print (file.tell())
# print (file.readline())
# position = file.tell()
# print (position)
# file.seek(position)
# file.write("This a new line added...\n")



line_number = 2 # desired line number 
file.seek(0)  # make sures that you are starting from the beginnig

for i in range (line_number-1):   # line_number -1 is because your line starts with 1
    file.readline()         # Reading the line till you reach that line number
position = file.tell()
print (position)
file.seek(position)
print (file.readline())
file.close()

# cant we skip to newline using seek
# what is the impact giving an arument to the method readlines 
