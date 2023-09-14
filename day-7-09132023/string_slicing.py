
"""
    strings , lists are iterable
    we can access them element by element

    individually accessing them would be possible by 
    giving the position number and
    we can get them in group by using slicing technique

    a = 'helloworld'
    print (a[0]+a[1]+a[2]+a[3]+a[4]+" "+a[5]+a[6]+a[7]+a[8]+a[9])
    "hello world"

"""

"""
    syntax :

        variable_name[<start>:<end>:<step>] - default - entire iterable
        start - index/position number from where you want to start
        end - index / position number till where you wan to access
        step - positive - same order as initialised
                negative - reverse order as initialised


        variable_name[]

        s - 0
        e - 10
        step - 2

"""





"""
variable_name[ start_index : end_index + 1 : step (positive/negative) ]

    start_index - index number you want to start the list
    end_index - index number till what value you want to 
                access the list
    step - how many numbers you want to consider after each number
            and positive number denotes access in the same order as initialised
            negative number denotes access in the reverse order

"""

a = '0123456789'

print (a[:])  
    # default       
    # start index   - 0
    # end index     - length of the list
    # step          - 1 (positive)
print (a[2:])
    # start index   - 2
    # end index     - length of the list
    # step          - 1 (positive)
print (a[:3])
    # start index   - 0
    # end index     - 3
    # step          - 1 (positive)
    # Here we will get from 0th element to element before
    # index 3, list will be printed in same order as initialised
print (a[::1])
print (a[::2])
    # start index   - 0
    # end index     - length of the list
    # step          - 2 (positive)
    # Here we will get from 0th element to end of the list
    # after each step 2nd element will be accessed 
    # list will be printed in same order as initialised
print (a[:2:2])
    # start index   - 0
    # end index     - 2
    # step          - 2 (positive)
    # Here we will get from 0th element to element before index 2
    # after each step 2nd element will be accessed
    # list will be printed in same order as initialised
# -----------------------------
print (a[::-1])
    # start index   - length of the list - 1
    # end index     - 0
    # step          - 1 (negative)
    # Here we will get from -1st element to -9th element
    # after each step, 1st element will be accessed 
    # list will be printed in same order as initialised

"""

0 1 2 3 4 5 6 7 8 9 (+)
| | | | | | | | | |
0 1 2 3 4 5 6 7 8 9
| | | | | | | | | |
109 8 7 6 5 4 3 2 1 (-)


0 1 2 3 4 5 6 7 8 9 (+)
| | | | | | | | | |
9 8 7 6 5 4 3 2 1 0
| | | | | | | | | |
109 8 7 6 5 4 3 2 1 (-)

<---------- (-1) step
----------> (+1) step

0  1   2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  
5, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95
18 17 16   15  14  13  12  11  10  9   8   7   6   5   4   3   2    1

list_variable[2:-3:1]

"""