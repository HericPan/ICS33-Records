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

    def __repr__(self):
        return 'prange('+str(self.start)+','+str(self.stop)+','+('' if self.step==1 else str(self.step))+')'
    
    def __iter__(self):

        class prange_iter:
            def __init__(self,start, stop, step):
                self.n = start
                self.stop = stop
                self.step = step
            
            def __next__(self):
                if self.step > 0 and self.n >= self.stop or \
                    self.step < 0 and self.n <= self.stop:
                    raise StopIteration
                save = self.n
                self.n += self.step
                return save
            def __iter__(self):
                return prange_iter(self.n, self.stop, self.step)
        
        return prange_iter(self.start, self.stop, self.step)
    
    def __next__(self):
        if self.step > 0 and self.n >= self.stop or \
           self.step < 0 and self.n <= self.stop:
            raise StopIteration
        save = self.n
        self.n += self.step
        return save

    def __len__(self):
        if self.step > 0 and self.start >= self.stop or \
           self.step < 0 and self.start <= self.stop:
            return 0
        else:
            return math.ceil((self.stop-self.start)/self.step)
              
    def __getitem__(self,n):
        if n < 0 or n >= len(self) :  # yes, could be n >= self.__len__()
            raise IndexError('range('+str(self)+') index('+str(n)+') out of range')
        return self.start+n*self.step
    
    def __contains__(self,n):
        if self.step > 0:
            return self.start<=n<self.stop and (n-self.start)%self.step == 0
        else:
            return self.stop<n<=self.start and abs(n-self.start)%abs(self.step) == 0
        
    def __reversed__(self):
        if self.step > 0:
            return prange(self.start+(len(self)-1)*self.step,self.start-1,-self.step)
        else:
            return prange(self.start+(len(self)-1)*self.step,self.start+1,-self.step)
