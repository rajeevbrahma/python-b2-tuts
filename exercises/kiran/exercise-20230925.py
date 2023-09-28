# avinash is Graduate with 85 %
# check if avinash is eligible to write the exam if 
# it has following criteria
# 1. should pass 12th with should have 65% - Company A
# 2. should be a graduate with 90% - Company B
# 3  should be a grduate with 85% - Company C
# 4. either 12th pass with 90% or graduate with 75% - - Company D

qualification='graduate'
grade=85

# Company A
if qualification=='intermediate' and grade>=65:
    print("You are qualified for company A")
else:
    print("You are not qualified for company A")

# Company B
if qualification=='graduate' and grade>=90:
    print("You are qualified for company B")
else:
    print("You are not qualified for company B")

# Company C
if qualification=='graduate' and grade>=85:
    print("You are qualified for company C")
else:
    print("You are not qualified for company C")

# Company D
if (qualification=='intermediate' and grade>=90) or (qualification=='graduate' and grade>=75):
    print("You are qualified for company D")
else:
    print("You are not qualified for company D")
