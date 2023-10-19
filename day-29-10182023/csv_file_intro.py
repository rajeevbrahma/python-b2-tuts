import csv 
from csv import writer, reader



# Create a file
# open("book.csv","x").close()


# # Open the file
# csv_file = open("movie_names.csv","w")
# csv_file.write("MovieName,Director,ReleaseYear\n")
# csv_file.write("The Shawshank Redemption,Frank Darabont,1994\n")
# csv_file.write("The Godfather,Francis Ford Coppola,1972\n")

# csv_file.close()

# # Open the file
# csv_file = open("book.csv","r")
# print (csv_file.read())
# csv_file.close()

# with csv module 

# Error examples


# Open the file
try:
    csv_file = open("movie_names.csv","w+")
# except FileExistsError as e:
#     print (e)
except FileNotFoundError as e:
    print (e)

csv_writer = writer(csv_file)
csv_writer.writerow(["MovieName","Director","ReleaseYear"])
csv_writer.writerow(["The Shawshank Redemption","Frank Darabont","1994"])
csv_writer.writerow(["The Godfather","Francis Ford Coppola","1972"])

# csv_file.close()

# csv_file = open("movie_names.csv","r")
# csv_file.seek(0)
csv_reader = reader(csv_file)
# print (csv_reader)

for row in csv_reader:
    print (row)


# try:
#     csv_writer.writerow(["The Shawshank Redemption","Frank Darabont"])
# except ValueError as e:
#     print (e)

# csv_writer.writerow(["The Godfather","Francis Ford Coppola","1972"])
csv_file.close()

# # Open the file
# csv_file = open("book.csv","r")
# csv_reader = csv.reader(csv_file)
# for row in csv_reader:
#     print (row)

# csv_file.close()

# # with csv module and list of dictionaries

# # Open the file
# csv_file = open("book.csv","w")
# csv_writer = csv.DictWriter(csv_file,fieldnames=["MovieName","Director","ReleaseYear"])
# csv_writer.writeheader()
# csv_writer.writerow({"MovieName":"The Shawshank Redemption","Director":"Frank Darabont","ReleaseYear":"1994"})
# try:
#     csv_writer.writerow({'1':'2',"MovieName":"The Godfather","Director":"Francis Ford Coppola","ReleaseYear":"1972"})
# except Exception as e:
#     print (e,type(e))
# csv_file.close()

# # Open the file
# csv_file = open("book.csv","r")
# csv_reader = csv.DictReader(csv_file)
# for row in csv_reader:
#     print (row)

# csv_file.close()

# # with csv module and list of dictionaries

# # Open the file
# csv_file = open("book.csv","w")
# csv_writer = csv.DictWriter(csv_file,fieldnames=["MovieName","Director","ReleaseYear"])
# csv_writer.writeheader()

# books = [{"MovieName":"The Shawshank Redemption","Director":"Frank Darabont","ReleaseYear":"1994"}]
# books.append({"MovieName":"The Godfather","Director":"Francis Ford Coppola","ReleaseYear":"1972"})
# csv_writer.writerows(books)
# csv_file.close()

# # Open the file
# csv_file = open("book.csv","r")
# csv_reader = csv.DictReader(csv_file)
# for row in csv_reader:
#     print (row)

# csv_file.close()

