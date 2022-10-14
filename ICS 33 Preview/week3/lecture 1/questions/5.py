'''
Created on 2020-8-18

@author: panru
'''
class C:
    instance_count = 0
    
    def __init__(self):
        C.instance_count += 1
        
a = C()
b = C()
print(C.instance_count) 
c = C()
print(C.instance_count) 