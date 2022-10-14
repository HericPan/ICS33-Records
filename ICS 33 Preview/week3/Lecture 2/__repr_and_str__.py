'''
Created on 2020-8-23

@author: panru
'''
import math

class Vector:
    
    def __init__(self, *args):
        self.coords = args
        
    def __len__(self):
        return len(self.coords)
    
    def __bool__(self):
        return any(c for c in self.coords)
    
    def __repr__(self):
        return 'Vector('+','.join(str(c) for c in self.coords)+")"
    
    def distance(self):
        return math.sqrt(sum(v**2 for v in self.coords))
    
    def __lt__(self, right):
        return self.distance() < right.distance()
    
    
    def __add__(self,right):
        if type(right) is Vector:
            assert len(self) == len(right), 'Vector.__add__: operand self('+str(self)+') has different dimension that operand right('+str(right)+')'
            return Vector( *(c1+c2 for c1,c2 in zip(self.coords,right.coords)) )
        elif type(right) in (int,float):
            return Vector( *(c+right for c in self.coords) )
        else:
            return NotImplemented

        
#     def __str__(self):
#         return 'Vector('+','.join(str(c) for c in self.coords)+")"
    
# v = Vector(0,0)
# x = repr('abc')
# print(type(x), x)
# x = str(v)
# print(type(x), x)
x = Vector(0,0)
y = Vector(2,2)
# print(x>15)
print(1+x)