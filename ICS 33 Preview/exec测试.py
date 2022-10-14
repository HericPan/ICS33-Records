'''
Created on 2020-7-27

@author: panru
'''
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2}, {'y'})
    
func()
