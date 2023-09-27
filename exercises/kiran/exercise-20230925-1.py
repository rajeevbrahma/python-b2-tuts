# avinash is Graduate with 85 %
# check if avinash is eligible to write the exam if 
# it has following criteria
# 1. should pass 12th and should have 65% - Company A
# 2. should be a graduate with 90% - Company B
# 3  should be a grduate with 85% - Company C
# 4. either 12th pass with 90% or graduate with 75% - - Company D

qualification='graduate'
grade=85

# Company A
if qualification=='intermediate': 
    if grade>=90:
        print("You are qualified for company D")
    if grade>=65:
        print("You are qualified for company A")
    else:
        print("You are not qualified for company A,B,C or D")


elif qualification=='graduate':
    if grade>=90:
        print("You are qualified for company B")
    if grade>=85:
        print("You are qualified for company C")
    if grade>=75:
        print("You are qualified for company D")
    else:
        print("You are not qualified for company B or C or D")
else:
    print("You are not qualified for company A or B or C or D")
    
