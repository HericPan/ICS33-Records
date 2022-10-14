'''
Created on 2020-9-2

@author: panru
'''
from collections import defaultdict

class C:
    def __init__(self):
        self._history = defaultdict(list)
        self.s = 0
    
    def bump(self):
        self.s += 1
        
    def __setattr__(self, name, value):
        # print('C.__setattr__', name, value)
        if '_history' in self.__dict__:
            self._history[name].append(value)
        self.__dict__[name] = value
    
    def report(self):
        print("History Report: ")
        for k,v in sorted(self._history.items()):
            print('\t', k, ' had the values:', v)

o = C()
o.a = 1
o.b = 2
o.c = 3
o.s = 4
o.a = 2
o.report()
o.bump()
o.report()