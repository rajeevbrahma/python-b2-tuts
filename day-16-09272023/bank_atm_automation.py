# Bank ATM Automation

X_BANK_NAME = "X Bank"
X_BANK_CODE = 1000
Y_BANK_NAME = "Y Bank"
Y_BANK_CODE = 1100

TRANSACTION_TYPE = ("DEPOSIT","WITHDRAWL")

"""                                 
    ACCOUNT NUMBER FORMAT = 12340001
                    bank_code -  first four digits
                    account number - last four digits
"""


transaction_history_template = {
    "type":None,
    "amount":None
}

bank_user_details_template  = {
        "first_name":None,
        "last_name":None,
        "account_number":None,
        "balance":None,
        "transaction_history":[
            transaction_history_template,
            transaction_history_template,
            transaction_history_template
        ]
    }

bank_user_details = {
  X_BANK_CODE :{
    "0000":bank_user_details_template  
  },
  Y_BANK_CODE:{
    "0000":bank_user_details_template
  }
}


while True:
    print ("Welcome to - ", X_BANK_NAME," ATM")
    print ("Enter your account number")
    account_number = input("Your bank number here - ")
    if (account_number[0:4] == X_BANK_CODE):
        print ("")
        transaction_option = input("Choose one option 1. Withdrawl 2.Deposit")
        if (transaction_option == 1):
            ...
        elif(transaction_option == 2):
            ...
    elif (account_number[0:4] == Y_BANK_CODE):
        print ("")