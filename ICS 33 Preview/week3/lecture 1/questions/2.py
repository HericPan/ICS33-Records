'''
Created on 2020-8-18

@author: panru
'''
class C:
    def __init__(self,a):
        self.a = a

x = C(1)
C.__init__(x,2)
print(x.a)