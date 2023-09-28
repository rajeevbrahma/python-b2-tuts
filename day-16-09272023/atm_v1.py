# Automatic Teller Machine Program

X_BANK_NAME = "X Bank"
Y_BANK_NAME = "Y Bank"
X_BANK_CODE = 1101
Y_BANK_CODE = 1201

atm_provided_banks = {
    X_BANK_CODE : (X_BANK_CODE,X_BANK_NAME),
    Y_BANK_CODE : (Y_BANK_CODE,Y_BANK_NAME)
}

AVAILABLE_ATM_CASH = 10000

transaction_template = {
    "is_deposit":None,
    "amount":None
}

customer_info_template = {
    "first_name":None,
    "last_name":None,
    "bank_info":atm_provided_banks[X_BANK_CODE],
    "balance":1000,
    "account_number":None,
    "transactions":[
        transaction_template,   # will always have the latest transaction
        transaction_template,
        transaction_template
    ]
}

# Your bank account number follows this sequence
# 11010012 - first four numbers represents the bank code and next four your account number

customers_info = {}
#     # key (account number) : value (customer_info_template with actual data)
    
# customer_info_template["first_name"] = "John"
# customer_info_template["last_name"] = "Doe"
# customer_info_template["bank_info"] = atm_provided_banks[X_BANK_CODE]
# customer_info_template["account_number"] = "11010012"
# customer_info_template["balance"] = 1000
# customer_info_template["transactions"] = []
# #insert the customer's in the customers_info dictionary
# customers_info[customer_info_template["account_number"][4:]] = customer_info_template

# customer_info_template = {}
# customer_info_template["first_name"] = "Patrick"
# customer_info_template["last_name"] = "Jane"
# customer_info_template["bank_info"] = atm_provided_banks[X_BANK_CODE]
# customer_info_template["account_number"] = "11010014"
# customer_info_template["balance"] = 1000
# customer_info_template["transactions"] = []
# customers_info[customer_info_template["account_number"][4:]] = customer_info_template

# customer_info_template = {}
# customer_info_template["first_name"] = "Teressa"
# customer_info_template["last_name"] = "Lisbon"
# customer_info_template["bank_info"] = atm_provided_banks[Y_BANK_CODE]
# customer_info_template["account_number"] = "12010032"
# customer_info_template["balance"] = 1000
# customer_info_template["transactions"] = []
# #insert the customer's in the customers_info dictionary
# customers_info[customer_info_template["account_number"][4:]] = customer_info_template

# customer_info_template = {}
# customer_info_template["first_name"] = "Kimbal"
# customer_info_template["last_name"] = "Cho"
# customer_info_template["bank_info"] = atm_provided_banks[Y_BANK_CODE]
# customer_info_template["account_number"] = "11010024"
# customer_info_template["balance"] = 1000
# customer_info_template["transactions"] = []
# customers_info[customer_info_template["account_number"][4:]] = customer_info_template

# # print (customers_info)


for customer_number in range(1,2):
    customer_info_template = {}
    print ("Enter Information for Customer ",customer_number)
    customer_info_template["first_name"] = input(" First Name here : ")
    customer_info_template["last_name"] = input(" Last Name here : ")
    bank_code = int(input("Enter your Bank code"))
    customer_info_template["bank_info"] = atm_provided_banks[bank_code]
    customer_info_template["account_number"] = input("Account Number here")
    customer_info_template["balance"] = input("Your Account Balance")
    customer_info_template["transactions"] = []
    customers_info[customer_info_template["account_number"][4:]] = customer_info_template
    print (customer_number)
print (customers_info)





"""
    11010012
        John Doe X bank, [],1000
    11010014
        Patrick Jane X bank, [],1000
    
    12010032
        Teressa Lisbon Y bank, [],1000
    12010024
        Kimbal cho Y bank, [],1000

"""




