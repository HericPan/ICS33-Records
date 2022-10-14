'''
Created on 2020-9-2

@author: panru
'''
from pip._internal import self_outdated_check
class Echo:
    def __init__(self, open_file):
        self._log_file = open_file
    
    def __enter__(self):
        import builtins, sys
        self._real_print = builtins.print
        def echo_print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
            self._real_print(*objects, sep=sep, end=end, file=file, flush=flush)
            self._real_print(*objects, sep=sep, end=end, file=self._log_file, flush=flush)
        builtins.print = echo_print
        return self
    
    def __exit__(self,exc,exc_value, traceback):
        import builtins
        self._log_file.close()
        builtins.print = self._real_print
        return True


with Echo(open('test_echo_output.txt','w')):
    print('abc')
    print(1,2,3)
    print('xyz')
    raise AssertionError
print('After with')