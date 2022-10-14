
from importlib import reload
import private
reload(private)
from private import C

# Test __setattr__
o=C()

o.add_more_attributes()
o.d = 5

o.a_private_is_ok_name = 1 # not START with private_
del o.__dict__['a_private_is_ok_name']

# Test __getattr__
o.bump() # also testing __seattr__, since self.a += 1 is like self.a = self.a + 1

private.__init__(o)



# Extra tests: Substituting methods in class C
import extra
C.__init__ = extra.__init__
C.add_more_attributes = extra.add_more_attributes
C.bad_add_more_attributes = extra.bad_add_more_attributes
C.bump = extra.bump
C.__str__ = extra.__str__

# Test __setattr__
o=C()
o.add_more_attributes()
o.o = 5

extra.extra_bump(o)
o.l_private_is_ok_name = 1 # not START with private_
del o.__dict__['l_private_is_ok_name']
# 
# # Test __getattr__
# c-->o.bump() # also testing __seattr__, since self.a += 1 is like self.a = self.a + 1
# ==-->o.__dict__-->{'private_l': 2, 'private_m': 3, 'n': 4, 'o': 5}
# e-->o.n-->4
# e-->o.o-->5
# ^-->o.l-->NameError
# ^-->o.m-->NameError
# e-->str(o)-->l=2,m=3,n=4,o=5
# ^-->private.f(o)-->NameError
# c-->private.__init__(o)
# ==-->o.__dict__-->{'private_l': 2, 'private_m': 3, 'n': 4, 'o': 5, 'z': 'z'}
