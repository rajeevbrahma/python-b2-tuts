from csv import writer, reader

#  ----- We can create and write to a csv file using csv module -----


# Open the file
try:
    csv_file = open("movie_names.csv","w+") # w+ mode creates the file if it does not exist
except FileExistsError as e:   # FileExistsError catches the error if the file already exists 
    print (e)
except FileNotFoundError as e: # FileNotFoundError catches the error if the file does not exist
    print (e)

csv_writer = writer(csv_file) # writer() returns a writer object which is used to write to the csv file
csv_writer.writerow(["MovieName","Director","ReleaseYear"]) # writerow() writes a row to the csv file
csv_writer.writerow(["The Shawshank Redemption","Frank Darabont","1994"]) # writerow() writes a row to the csv file
csv_writer.writerow(["The Godfather","Francis Ford Coppola","1972"]) # writerow() writes a row to the csv file


# The following writerow will throw an error because the number 
# of elements in the list is not equal to the number of fields

try:
    csv_writer.writerow(["The Shawshank Redemption","Frank Darabont"])
except ValueError as e:
    print (e)

csv_file.close() # close the file


csv_file = open("movie_names.csv","r") # open the file in read mode
csv_file.seek(0)   # seek() sets the file's current position to the beginning of the file
csv_reader = reader(csv_file) # reader() returns a reader object which is used to read from the csv file

for row in csv_reader: # iterate over the reader object
    print (row) # print each row

