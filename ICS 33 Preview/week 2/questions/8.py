'''
Created on 2020-8-13

@author: panru
'''
import re

def contract(string):
    return re.sub(r'(\w)\1+', '\g<1>', string)

print(contract('It is a goooooal! A gooal.'))
    