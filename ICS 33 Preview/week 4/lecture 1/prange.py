from goody import type_as_str
import math
class prange:
    def __init__(self,*args):
        for a in args:
            if not type(a) is int:
                raise TypeError('\''+type_as_str(a)+'\' object cannot be interpreted as an integer')

        self.start, self.step = 0,1   # defaults
        if len(args) == 1:
            self.stop = args[0]                       # store single argument
        elif len(args) == 2:
            self.start, self.stop = args              # unpack 2 arguments
        elif len(args) == 3:
            self.start, self.stop, self.step = args   # unpack 3 arguments
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
            if self.step == 0:
                raise ValueError('3rd argument must not be 0')
        else:
            raise TypeError('range expected at most 3 arguments, got '+str(len(args))) 

        # store exactly the range of values into a list
        self.listof = []
        self.n = self.start
        while True:
            if self.step > 0 and self.n >= self.stop or \
               self.step < 0 and self.n <= self.stop:
                break
            self.listof.append(self.n)
            self.n += self.step

    def __repr__(self):
        return 'prange('+str(self.start)+','+str(self.stop)+','+('' if self.step==1 else str(self.step))+')'
    
    def __iter__(self):
        return iter(self.listof)
    
    # no need to define __next__: __iter__ returns iter(list) and list defines __next__

    def __len__(self):
        return len(self.listof)
              
    def __getitem__(self,n):
        return self.listof[n] 
       
    def __contains__(self,n):
        return n in self.listof
            
    def __reversed__(self):
        return reversed(self.listof)

    
for i in prange(6, 0, -1):
    print(i)