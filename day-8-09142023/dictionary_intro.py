"""
We can store the data in key value pairs.They are changeable and duplicates are not allowed
    example :{
        key:value
    }
    "key"   - allowed data types : numbers,strings
    "value" - allowed data types : numbers,strings,lists,dictionaries,boolean,none



    A Dictionary will have 
            word : and its respective meaning

    Like the same way dictioinaries in Python will be have 
        key_name : and its associated value

    How can we relate dictionaries with List

    In list we associate list elements with the index and dictionaries we associate
    dictionary values with keys.

    In list we are accessing list elements with its respective index number
    In dictionary we can access values with its respective key name

   Symbol ":" (colon) will be used to seperate key and its value

   In List we seperate each element with symbol ","(comma) In the same way we 
   seperate dictionary elements using same symbol "," (comma) 
  
  List Example:
        ["Eric","Clapton",78,'30 Mar']
            0       1      2    3
        {
            "first_name":"Eric",
            "last_name":"Clapton",
            "age":78,
            "dob":"30 Mar"
        }

"""



"""
john_bank_details
        bank_names = X, Y - list
        pin = 3454,3345 - list
        amount = 456   - Integer
        name = John    - String
"""

loan_details = 'john_loan_details'
john_bank_details = {
    'name':"John",
    'amount':456,
    'pin':[
        3455,
        3434
    ],
    'bank_names':[
        'X',
        'Y'
    ],
    'cvv':{
        'X':267,
        'Y':234
    },
    "is_credit":{
        'X':True,
        'Y':False
    },
    loan_details:{
        'X':None,
        'Y':1
    }
}

print (john_bank_details)
print ("Type of John bank details - ",type(john_bank_details))
print (john_bank_details['bank_names'])
print ("Type of John bank details, value associated to bank_names - ",type(john_bank_details['bank_names']))
print (john_bank_details['name'])
print ("Type of John bank details, value associated to name - ",type(john_bank_details['name']))
print (john_bank_details['amount'])
print ("Type of John bank details, value associated to amount - ",type(john_bank_details['amount']))
print   as