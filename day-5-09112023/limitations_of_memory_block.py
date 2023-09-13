
# This program is under experimenting stage please ignore while learning


"""
    simple strings without spaces( ) will have same memoryblock
"""
a = 'hello '
b = 'hello '
print (id(a),id(b))

"""
    strings with spaces( ) will NOT have same memoryblock
"""
d = c = 'hello world'
print (id(c),id(d))
f = 'hello world'
print (id(f))

e = 257023456345634
f = 257023456345634
print (id(e),id(f))