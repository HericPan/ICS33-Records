'''
Created on 2020-8-13

@author: panru
'''
import re
  
def grep(pattern, filename):
    with open(filename) as infile:
#         print([m for m,n in enumerate([line.rstrip() for line in infile], 1)])
        return tuple((filename,n,m) for m,n in enumerate([line.rstrip() for line in infile], 1) if (re.match(pattern, n) != None))


print(grep('abcdefg', 'abc.txt'))






