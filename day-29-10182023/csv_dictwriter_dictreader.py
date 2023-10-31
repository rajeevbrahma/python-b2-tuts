""" DictWriter and DictReader Examples """
from csv import DictWriter, DictReader


# with csv module and dictionary

# Open the file
csv_file = open("list_of_dictionaries_example_file.csv","w") # w write only mode
# creating DictWriter object with fieldnames as the first row
csv_dict_writer = DictWriter(csv_file,fieldnames=["MovieName","Director","ReleaseYear"])
csv_dict_writer.writeheader() # writeheader() writes the fieldnames as the first row

# writerow() writes a row to the csv file
csv_dict_writer.writerow({"MovieName":"The Shawshank Redemption","Director":"Frank Darabont","ReleaseYear":"1994"})
csv_dict_writer.writerow({"MovieName":"Movie 2 ","Director":"Director 2","ReleaseYear":"1728"})
csv_dict_writer.writerow({"MovieName":"Movie 3 ","Director":"Director 3","ReleaseYear":"1273"})

# The following writerow will throw an error because the dictionary
# keys are not equal to the fieldnames
try:
    csv_dict_writer.writerow({'1':'2',"MovieName":"The Godfather","Director":"Francis Ford Coppola","ReleaseYear":"1972"})
except Exception as e:
    print (e,type(e))

csv_file.close()


# Open the file
csv_file = open("movie_names_dict_writer_reader.csv","r")

csv_dict_reader = DictReader(csv_file)
print (csv_dict_reader)
print (csv_dict_reader.line_num) # Gives line number
for row in csv_dict_reader:
    if (csv_dict_reader.line_num == 3):
        print (csv_dict_reader.line_num)
        print (row)
        print (row["MovieName"])
        print (row["Director"])
        print (row["ReleaseYear"])
        
csv_file.close()


# with csv module and list of dictionaries

# Open the file
csv_file = open("book.csv","w")
csv_writer = DictWriter(csv_file,fieldnames=["MovieName","Director","ReleaseYear"])
csv_writer.writeheader()

books = [{"MovieName":"The Shawshank Redemption","Director":"Frank Darabont","ReleaseYear":"1994"}]
books.append({"MovieName":"The Godfather","Director":"Francis Ford Coppola","ReleaseYear":"1972"})
csv_writer.writerows(books)
csv_file.close()


# ------ Example -----------

# when the data given to you in the list of dictionary format
data = [
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
    {'s.no':1,'a':234,'b':234},
]

file = open("bank_data.csv","w")
csv_writer = DictWriter(file,fieldnames=['s.no','no.of.atms','max amount','city code'])
csv_writer.writerows(data)
