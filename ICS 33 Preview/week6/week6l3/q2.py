from bst import TN
import bst

def sum_T(atree):
    if atree == None:
        return 0
    else:
        return atree.value + sum_T(atree.left) + sum_T(atree.right)

t = TN(2)
t = bst.add(t, 1)
t = bst.add(t, 3)
t = bst.add(t, 4)

print(sum_T(t))