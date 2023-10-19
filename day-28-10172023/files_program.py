
# import time 



# # different methods that you can apply on an opened file
# # write, read, tell, seek, close, flush writelines, readline readlines ....



# # Open a file 

file_with_write_and_read = open("book.txt",'w+')  # write and read
# when you open a file in write mode, it will create a new file if it does not exist
file_with_write_and_read.write("This is first line\n") # write to the file
file_with_write_and_read.write("This is second line\n") # write to the file

# print (file_with_write_and_read.read()) # reads the entire file

file_with_write_and_read.close() # close the file

file_with_read_and_write = open("book.txt","r+") # read and write 
# when you open a file in read mode, it will throw an error if it does not exist

file_with_read_and_write.seek(0) # move the cursor to the beginning of the file
print (file_with_read_and_write.readline()) # read a line from the file
file_with_read_and_write.seek(19) # move the cursor to the 19th character of the file
print (file_with_read_and_write.readline()) # read a line from the file

file_with_read_and_write.write("This is third line\n") # write to the file
file_with_read_and_write.write("This is fourth line\n") # write to the file
file_with_read_and_write.close() # close the file


file_with_write_only = open("book_2.txt","w") # write only
# when you open a file in write mode, it will create a new file if it does not exist
file_with_write_only.write("This is first line\n") # write to the file
file_with_write_only.write("This is second line\n") # write to the file
print ("File is Writable - ",file_with_write_only.writable()) # check if the file is writable
print ("File is readable - ",file_with_write_only.readable()) # check if the file is readable
file_with_write_only.close() # close the file

file_with_read_only = open("book_2.txt","r") # read only
# when you open a file in read mode, it will throw an error if it does not exist
print (file_with_read_only.read()) # reads the entire file
print ("File is Writable - ",file_with_read_only.writable()) # check if the file is writable
print ("File is readable - ",file_with_read_only.readable()) # check if the file is readable
file_with_read_only.close() # close the file


file_with_write_and_read = open("book_3.txt",'w+')  # write and read

file_with_write_and_read.write("This is first line\n") # write to the file
file_with_write_and_read.write("This is second line\n") # write to the file

file_with_write_and_read.flush() # flush the buffer to the file immediately
time.sleep(2) # sleep for 10 seconds
file_with_write_and_read.write("This is third line\n") # write to the file
file_with_write_and_read.write("This is fourth line\n") # write to the file
file_with_write_and_read.close() # close the file


# readline example
file_with_read_only = open("book_2.txt","r") # read only
# when you open a file in read mode, it will throw an error if it does not exist
# readline reads a single line from the file
print (file_with_read_only.readline()) # reads the first line from the file
print (file_with_read_only.readline()) # reads the second line from the file

file_with_read_only.close() # close the file

# readlines example
file_with_read_only = open("book_2.txt","r") # read only
# when you open a file in read mode, it will throw an error if it does not exist
# readlines reads all the lines from the file and returns a list of lines
print (file_with_read_only.readlines()) # reads all the lines from the file

file_with_read_only.close() # close the file


# seek example
file_with_read_only = open("book_2.txt","r") # read only

print (file_with_read_only.tell()) # tells the current position of the cursor
file_with_read_only.seek(3) # move the cursor to the beginning of the file
print (file_with_read_only.tell()) # tells the current position of the cursor
file_with_read_only.seek(4) # move the cursor to the beginning of the file
print (file_with_read_only.tell()) # tells the current position of the cursor

file_with_read_only.close() # close the file


# tell example
file_with_read_only = open("book.txt","r") # read only

print ("The curosor is at ",file_with_read_only.tell()) # tells the current position of the cursor
file_with_read_only.seek(3)
print ("The curosor is at ",file_with_read_only.tell()) # tells the current position of the cursor

file_with_read_only.close() # close the file


#write lines example

file_with_write_only = open("book_2.txt","w") # write only

file_with_write_only.writelines(["This is first line\n",
                                 "This is second line\n",
                                 "This is third line\n",
                                 "This is fourth line\n",
                                 "This is fifth line\n",]) # write to the file

print (file_with_write_only.readable())

import io 
try:
    print (file_with_write_only.readlines()) # reads all the lines from the file
except io.UnsupportedOperation as e:
    print ("Error caught ---",e)
except Exception as e:
    print ("Errror----",e,type(e))
file_with_read_only.close() # close the file
print ("File Closed")



try:
    file_with_read_only_when_the_file_doesnt_exist = open("book_5.txt","r") # read only
except FileNotFoundError:
    print ("file not found and i am going to create it here")
    try:
        open("book_4.txt","x")
    except FileExistsError:
        print ("Looks like the file is already existed .. .\n")
        file_name = input("Enter a new file name -- ")
        open(file_name,"x")


# file_with_read_only_when_the_file_doesnt_exist = open("book_4.txt","r")
# print (file_with_read_only_when_the_file_doesnt_exist.seek(0))


# Create a Certificate file with the following template and generate certificates for all the class people
# Create an email template seeking leave 
#   manager name
#   reason
#   leave type
#   leave duration
#   your name

# What is your manager name - Mark 
# What is reason for your leave - Nothing 
# Leave type - Casual Leave / Sick Leave / Vacation 
# leave duration - 14th Aug to 14 Sep 
# your name - John

