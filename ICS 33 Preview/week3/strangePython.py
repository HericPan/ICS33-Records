'''
Created on 2020-8-18

@author: panru
'''
class C:
    def __init__(self, init_attr):
        self.instance_attr = init_attr
        
    def getnum(self):
        print(self.instance_attr)

def setnum(self, num):
    self.instance_attr = num
    
o = C(20)
o.getnum()
o.setnum = setnum
o.setnum(o, 30)
o.getnum()
o1 = C(30)
# o1.setnum(30)
print(o)
