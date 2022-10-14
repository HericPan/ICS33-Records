'''
Created on 2020-9-2

@author: panru
'''
class Ignore:
    # no 2nd argument means ignore ALL exceptions
    def __init__(self,*exceptions_to_ignore):
        self._ignore = exceptions_to_ignore
    
    def __enter__(self):
        return self
    
    def __exit__(self,exc,exc_value,traceback):
        return self._ignore == () or exc in self._ignore
    
with Ignore(AssertionError):
    raise TypeError('...')
print('After with')