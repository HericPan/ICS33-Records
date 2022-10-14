'''
Created on 2020-8-18

@author: panru
'''
class C:
    def __init__(self, low, high):
        assert low < high, 'the lower one is bigger than the higher one'
        self.low = low
        self.high = high
        
o = C(1,2)
p = C(2,1)
        