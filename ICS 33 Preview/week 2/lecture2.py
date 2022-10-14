'''
Created on 2020-8-13

@author: panru
'''
import re

phone = r'^(?:\((\d{3})\))?(\d{3})[-.](\d{4})$'
m = re.match(phone, '(949)824-2709')
print(m)
assert m != None, 'No match'
print(m.groups())

area, exchange, number = [int(i) if i != None else None for i in m.group(1,2,3)]
print(area, exchange, number)

# 
# print(re.split('(?:;+)', 'abc;d;;e'))


# print( re.sub('(a+)','\g<1>KK','aabcaaadaf'))

# print( re.subn('(a+)','{as}','aabcaaadaf'))

# print(len('\*'))