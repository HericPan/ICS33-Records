'''
Created on 2020-9-2

@author: panru
'''
class C:
    def __getattr__(self, name):
        print('Attribute for ' + name + ' not found')
        print(type(name))
        return name+'?'

o = C()
print(o.a_name)
print(o.a_name)
o.a_name = 0
print(o.a_name)