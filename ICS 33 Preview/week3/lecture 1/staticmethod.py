'''
Created on 2020-8-18

@author: panru
'''
import math

class Point2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def from_polar(dist,angle):
        
        return Point2d( dist*math.cos(angle), dist*math.sin(angle) )
    
    @staticmethod
    def _distance(x1,y1,x2,y2):
        return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

    def dist(self,another):
        return Point2d._distance(self.x, self.y, another.x, another.y)

o = Point2d(1,1)
b = Point2d(2,2)
print(o.dist(b))