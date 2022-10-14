from predicate import is_prime
from bst import TN
import bst

def all_satisfy(atree, f):
    if atree == None:
        return True
    else:
        return f(atree.value) and all_satisfy(atree.left, f) and all_satisfy(atree.right, f)
t = TN(2)
t = bst.add(t, 7)
t = bst.add(t, 3)
t = bst.add(t, 5)

print(all_satisfy(t, is_prime))