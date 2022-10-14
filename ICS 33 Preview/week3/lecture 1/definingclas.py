'''
Created on 2020-8-17

@author: panru
'''
class C:
    def __init__(self, p1):
        print('instance of C object initialized')
        self.a = 'starting' # initialize an instance/attribute name
        self.b = p1         # initialize an instance/attribute name

D = C    # Names C and D refer to (share) the same class object
x = C(1) # Use C to construct a first instance of a class C object (direct)
y = D(2) # Use D to construct another instance of a class C object (via sharing)

print(C,D,x,y)
print(type(x), type(y), type(C), type(type(x)))
