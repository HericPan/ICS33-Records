from bst import TN
import bst

def all_less(atree, value):
    if atree == None:
        return True
    else:
        return all_less(atree.left, value) and all_less(atree.right,value) if value > atree.value else False
def all_greater(atree, value):
    if atree == None:
        return True
    else:
        return all_greater(atree.right, value) and all_greater(atree.left, value) if value < atree.value else False

def is_bst(atree):
    if atree == None:
        return True
    return all_less(atree.left, atree.value) and all_greater(atree.right, atree.value) and is_bst(atree.left) and is_bst(atree.right)

t = TN(5)
t.left = TN(3)
t.left.right = TN(8)

print(is_bst(t))
