from prange import prange
from repea import Repeat
from Unique import Unique
from Filter import Filter
class psorted: # pseudo-sorted: works just like sorted
    def __init__(self, iterable, key=None, reverse=False):
        self.result = list(iterable)  # put all values from iterable into a list
        self.result.sort(key=key, reverse=reverse)
        
    def __iter__(self):
        return iter(self.result)                # so return in another statement

class preversed:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __iter__(self):
        class preserved_iter:
            def __init__(self, iterable):
                self.iterable = iterable
                self.count = len(iterable) - 1
        
            def __next__(self):
                if self.count < 0:
                    raise StopIteration
                answer = self.iterable[self.count]
                self.count -= 1
                return answer
        return preserved_iter(self.iterable)

for x in preversed([1,2,3,4,5,6]):
    print(x)