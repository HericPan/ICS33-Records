'''
Created on 2020-9-2

@author: panru
'''
from collections import defaultdict

class Count_Argument_Use:
    
    def __init__(self, func):
        self._func = func
        self._num_dict = defaultdict(int)
        
    def __call__(self, n):
        self._num_dict[n] += 1
        return self._func(n)
    
    def report(self):
        
#         self._report = [(arg, count) for arg, count in sorted(self._num_dict.items(), key=lambda key: (-key[1],key[0]))]
        print("%-9s|%13s\n---------+-------------" % ("Argument", "Times Called"))
#         i_love_one_line_OHHHHHHHH = [print("%9d|%13d" % (arg, count)) for arg,count in self._report]
        hey_pattis_can_you_see_this_i_love_one_line_OHHHHHHHHHHHHH = [print("%9d|%13d" % (arg, count)) for arg,count in [(arg, count) for arg,count in sorted(self._num_dict.items(), key=lambda key: (-key[1],key[0]))]]
    

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = Count_Argument_Use(fib)
fib(10)
fib.report()
