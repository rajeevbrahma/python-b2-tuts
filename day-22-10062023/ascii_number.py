""" function which returns ASCII number of a character"""

character_dictionary = {
    'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,
    'h':104,'i':105,'j':106,'k':107,'l':108,'m':109,'n':110,
    'o':111,'p':112,'q':113,'r':114,'s':115,'t':116,'u':117,
    'v':118,'w':119,'x':120,'y':121,'z':122,
    'A':65,'B':66,'C':67,'D':68,'E':69,'F':70,'G':71,
    'H':72,'I':73,'J':74,'K':75
}



#  dictionary - character as key and its respective ascii as value


# Define a function which takes a character as input 
# returns the ASCII number of a character

# definition of function
def return_ascii(character):
    """ Returns ascii   """
    # conditino statement 
    if len(character) == 1:
        return character_dictionary[character]
    else:
        return "Only accepts character with length 1"
    
print (return_ascii('a')) # function call
print (return_ascii('aa')) # function call
print (return_ascii('A')) # function call


