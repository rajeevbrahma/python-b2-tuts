import csv 
from csv import writer, reader


# ----- We can create and write to a csv file without using csv module -----
# Create a file
open("csv_file_created_without_using_csv_module.csv","x").close()


# Open the file
csv_file = open("csv_file_created_without_using_csv_module.csv","w")
csv_file.write("MovieName,Director,ReleaseYear\n")
csv_file.write("The Shawshank Redemption,Frank Darabont,1994\n")
csv_file.write("The Godfather,Francis Ford Coppola,1972\n")

csv_file.close()

# Open the file
csv_file = open("csv_file_created_without_using_csv_module.csv","r")
print (csv_file.read())
csv_file.close()


# csv methods
# writerow()    # writes a row to the csv file
# writerows()   # writes multiple rows to the csv file
# writer()    # returns a writer object which is used to write to the csv file
# reader()  # returns a reader object which is used to read from the csv file
# DictWriter()  # returns a DictWriter object which is used to write to the csv file
# DictReader()  # returns a DictReader object which is used to read from the csv file
# writeheader() # writes the fieldnames as the first row
# line_num # gives the line number
# seek()    # sets the file's current position to the number specified
# tell()   # returns the file's current position
# close() # closes the file
