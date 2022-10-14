class Percent_Histogram:
    def __init__(self,init_percents=[]):
        self._histogram = 10*[0]    # [0,0,0,...,0,0] length 10, all 0s
        for p in init_percents:
            self.tally(p)
         
    # Called only when 0<=p<=100: 100//10 is 10 but 100 belongs in index 9
    def _tally(self,p):
        self._histogram[p//10 if p<100 else 9] += 1
    
    def clear(self):
        for i in range(10):         # could write: self._histogram = 10*[0]
            self._histogram[i] = 0

    # tally allows any number of arguments, collected into a tuple by *args
    def tally(self,*args):
        if len(args) == 0:
            raise IndexError('Percent_Histogram.tally: no value(s) to tally')
        for p in args:
            if 0 <= p <= 100:
                self._tally(p)
            else:
                raise IndexError('Percent_Histogram.tally: '+str(p)+' outside [0,100]')
                # Another approach would be to store/remember all tally failures

    # allow indexing for bins [0-9]
    # but can mutate these values only through __init__, clear, and tally
    # no __setitem__ defined
    def __getitem__(self,bin_num):
        bin = (bin_num if bin_num >= 0 else 10-bin_num)
        if 0 <= bin <= 9:
            return self._histogram[bin]
        else:
            raise IndexError('Percent_Histogram.__getitem__: '+str(bin_num)+' outside [0,9]')

    # standard __iter__: defines a class with __init__/__next__ and returns
    #   an object from that class
    def __iter__(self):

        class PH_iter:
            def __init__(self,histogram):
                self._histogram = histogram          # sharing; sees mutation
                # self._histogram = list(histogram)  # copying; doesn't see it
                self._next = 0

            def __next__(self):
                if self._next == 10:
                    raise StopIteration
                answer = self._histogram[self._next]
                self._next += 1
                return answer

            def __iter__(self):
                return self

        return PH_iter(self._histogram)
            
    # To reconstruct a call the __init__ that reproduces the correct counts in
    #   the histogram, we supply the correct number of values, but all at the
    #   start of the bin: e.g., if bin 5 has 3 items, the repr has three 50s
    def __repr__(self):
        param = []
        for i in range(10):
            param += self[i]*[i*10]
        return 'Percent_Histogram('+str(param)+')'
    
    # a 2-dimensional display; do you understand the use of .format here?
    def __str__(self):
        return '\n'.join(['[{l: >2}-{h: >3}] | {s}'.format(l=10*i,h=10*i+9 if i != 9 else 100,s=self[i]*'*') for i in range(10)])