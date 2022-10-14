class TN:
    def __init__(self: "TN",
                 value : object, left : "TN" = None, right : "TN" = None):
        self.value = value
        self.left = left
        self.right = right

def size(atree):
    if atree == None:
        return 0
    else:
        return 1 + size(atree.left) + size(atree.right)

def height(atree):
    if atree == None:
        return -1
    else:
        return 1 + max( height(atree.left), height(atree.right))

def search(atree, value):
    if atree == None or atree.value == value:
        return atree
    else:
        return search((atree.left if value < atree.value else atree.right), value)

def add(atree, value):
    if atree == None:
        return TN(value)
    elif value == atree.value:
        return atree
    else:
        if value < atree.value:
            atree.left = add(atree.left, value)
        else:
            atree.right = add(atree.right, value)
        return atree