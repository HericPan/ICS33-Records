'''
Created on 2020-10-5

@author: panru
'''

def double(n):
    return 2*n

def triple(n):
    return 3*n

def times10(n):
    return 10*n

def call(func_name, n):
    return eval(func_name+"("+str(n)+")")

print(call('triple',5))