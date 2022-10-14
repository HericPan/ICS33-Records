'''
Created on 2020-8-17

@author: panru
'''
class C:
    x = 1
    def __init__(self, i):
        
        y = i
        
    def abc(self):
        pass

o = C(2)
o.x += 1
C.x += 2
print(o.__dict__)
print(C.__dict__)