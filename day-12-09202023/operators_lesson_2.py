# Identity operator 
# is, is not
# checks whether two operands(variables / literal) shares the exact
# same location
# It returns True when the operands share the same location, false 
# when they are not
a = 4
b = 4
a is b

# Membership opeartor
# in, not in
# checks whether operand 2 is part of operand 1 (varaiables / literal)
# condition : operands should be iterable (strings/lists/tuples/set)
# it returns True when it finds operand 2 in operand 1 and returns false
# when not found

# invalid usage
a = 56
b = 6
b in a

a = 'hello'
b = 'el'
c = 'O'
b in a
c not in a


"""
    1 2 3 4 
    a b c d - ascii - 

    1 - True / Enabled
    0 - False / Disabled
    
    <-------------------------
  2^7   ------  -   2^2  2^1  2^0
                      4 +  2 +  1  
                      0   0    0  - 0
                      0   0    1  - 1
                      0   1    0  - 2
                      0   1    1  - 3
                      1   0    0  - 4
                      1   0    1  - 5
                      1   1    0  - 6
                      1   1    1  - 7


5 & 7
101  111

1 0 1
1 1 1 (&)
---------
1 0 1

1 0 1
1 1 1 (|)
--------
1 1 1

2 | 2 

0 1 0 
0 1 0  (|)
-------
0 1 0 - 2

0 1 0 
0 0 1 (&)
-------
0 0 0  - 0  



Truth Tables

And     (&)
    -------
         (R)
     0 0 - 0
     0 1 - 0
     1 0 - 0
     1 1 - 1

OR      (|)
    -------
         (R)
     0 0 - 0
     0 1 - 1
     1 0 - 1
     1 1 - 1



<< 
>>

2 << 1
0 1 0  << 1
-----------
1 0 0  -  4

4 >> 2
7 >> 3 ,  7 << 3
                        

"""
a = 5
gender = 'M'

not (a > 5 and a < 14 and (gender == 'M' or gender =='F'))
                            False        True
     False       True                 True
True

Then
    print ("You are allowed to play")

debts > 100

debts_a = 190

if (not(debts_a > 100)):
    print ("give him account")
else:
    print ("Please!! Dont come again")

"""

    Even Numbers in the range 10 to 100
    Odd Numbers in the range 200 to 300
    Numbers divisble by 5 within 1 to 1000
    Number either divisible by 7 or 3

Operators 
    Arithmetic operator %
    Comparision operator (==)
                        (<,>)
    logical operators (and)

    a = 10
    a%2 == 0 and (a>10 and a<100)
    


"""