'''
Created on 2020-9-2

@author: panru
'''
class Store_Once:
    def __init__(self, *string_list):
        self.set = {str for str in string_list}
    
    def __setattr__(self, name, value):
        if name not in self.__dict__:
            self.__dict__[name] = value
        elif self.__dict__[name] is value:
            print("Good to go!")
        else:
            raise Exception("Rebound is not allowed!")
    

o = Store_Once('abc', 'abc','asdf')
print(o.set)
o.set = o.set
o.set = 'afdsaf'