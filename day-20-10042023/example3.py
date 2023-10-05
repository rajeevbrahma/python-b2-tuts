

# 1. you can import the whole program - you will get all the functions and variables defined within that program
# can be accessible from here
# 2. you can import the desired functions 
# 3. while importing you can give different name than the actual definition name
# import calculator # 1. importing whole program

# calculator.add(1,2)

from calculator import add as addition



def add(a,b,c,d,e):
    return a+b+c+d+e

addition(1,2)
# sub(2,1)
# mul(3,4)

# 1. define a function which takes two arguments(numbers) and return argument 1 to the power of argument 2


# function definition
def power_calc(base,power):
    return base ** power   

base = 2
power = 4

res1 = power_calc(2,4) # function call
res2 = power_calc(3,2) # function call
print (res1,res2)
print (power_calc(4,2)) # function call

# 2. define a function which takes zero arguments and return None function name - do_nothing

# 3. define a function which takes three keyword arguemnts and return this eqautions result
#   a + (b*c) 





