import inspect
class C:
    def __init__(self):
        self.__a  = 1
    
    def __setattr__(self, name, value):
        print(inspect.stack()[1].function)

x = C()
