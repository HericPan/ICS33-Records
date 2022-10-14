# Submitter: ruohuaip(Pan, Ruohuai)
# Partner  : haoyuaz9(Zhang, haoyuan)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt
from goody import type_as_str

class Sparse_Matrix:

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'

    def __init__(self, rows, cols, *vectors):
        # Assertions
        # 1. The row and cols arguments must be integers that are strictly greater than 0
        assert type(rows) == int and type(cols) == int and rows > 0 and cols > 0
        self.rows = rows
        self.cols = cols
        # 2. The row and column in each triple must be non-negative integers
        for v in vectors:
            assert v[0] >= 0 and v[1] >= 0 and v[0] < self.rows and v[1] < self.cols
        # 3. The row and column in each triple must be unique
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                assert not (vectors[i][0] == vectors[j][0] and vectors[i][1] == vectors[j][1])
        # 4. The value in each triple must be numeric (an int or float)
        for v in vectors:
            assert type(v[2]) in (int, float)
        self.matrix = dict()
        
        for v in vectors:
            if v[2] != 0: self.matrix[(v[0], v[1])] = v[2] 
            
    def size(self):
        return (self.rows, self.cols)
    
    def __len__(self):
        return self.rows * self.cols
    
    def __bool__(self):
        return len(self.matrix) != 0
    
    def __repr__(self):
        return "Sparse_Matrix(" + ", ".join([str(self.rows), str(self.cols)] + list(str((k[0], k[1], v)) for k,v in self.matrix.items())) +")"
    
    def __getitem__(self, i):
        if type(i) == tuple and len(i) == 2 and type(i[0]) == int and type(i[1]) == int and 0 <= i[0] < self.rows and 0 <= i[1] < self.cols:
            return self.matrix.get(i, 0)
        else:
            raise TypeError("The arguments are illegal.")
        
    def __setitem__(self, i, v):
        if type(i) == tuple and len(i) == 2 and type(i[0]) == int \
        and type(i[1]) == int and 0 <= i[0] < self.rows and 0 <= i[1] < self.cols \
        and type(v) in (int, float):
            if v != 0: 
                self.matrix[i] = v
            else:
                if i in self.matrix: self.matrix.pop(i)
        else:
            raise TypeError("The arguments are illegal.")
    
    def __delitem__(self, i):
        if type(i) == tuple and len(i) == 2 and type(i[0]) == int and type(i[1]) == int and 0 <= i[0] < self.rows and 0 <= i[1] < self.cols:
            if i in self.matrix: self.matrix.pop(i)
        else:
            raise TypeError("The arguments are illegal.")
    
    def row(self, r):
        assert type(r) == int and r < self.rows and r >= 0
        return tuple(self[r,c] for c in range(self.cols))
    
    def col(self, c):
        assert type(c) == int and c < self.cols and c >= 0
        return tuple(self[r,c] for r in range(self.rows))
    
    # '3x3 -> {(0, 0): 1, (1, 1): 5, (2, 2): 1} -> ((1, 0, 0), (0, 5, 0), (0, 0, 1))'
    def details(self):
        return f'{self.rows}x{self.cols} -> ' + str(self.matrix) + " -> (" + ', '.join(str(self.row(r)) for r in range(self.rows)) + ")"
    
    def __call__(self, r, c):
        assert type(r) == int and type(c) == int and r > 0 and c > 0
        d = dict(self.matrix)
        for v in self.matrix:
            if v[0] >= r or v[1] >= c:
                d.pop(v)
        self.__dict__.clear()
        self.rows = r
        self.cols = c
        self.matrix = d
    
    def __iter__(self):
        def gen(m):
            for v in sorted(m.matrix, key=(lambda k: m.matrix[k])):
                yield (v[0], v[1], m.matrix[v])
        return gen(self)

    def __pos__(self):
        return Sparse_Matrix(self.rows, self.cols, *tuple((k[0], k[1], self.matrix[k]) for k in self.matrix))
    
    def __neg__(self):
        return Sparse_Matrix(self.rows, self.cols, *tuple((k[0], k[1], -self.matrix[k]) for k in self.matrix))
    
    def __abs__(self):
        return Sparse_Matrix(self.rows, self.cols, *tuple((k[0], k[1], abs(self.matrix[k])) for k in self.matrix))
    
    def __add__(self, right):
        if type(right) not in (int, float, Sparse_Matrix):
            raise TypeError("unsupported operand type(s) for +: '" + "Sparse_Matrix" + "' and '" + type_as_str(right) +"'")
        elif type(right) in (int, float):
            s = Sparse_Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    s[r,c] = self[r,c] + right
        elif type(right) == Sparse_Matrix:
            assert self.rows == right.rows and self.cols == right.cols
            s = Sparse_Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    s[r,c] = self[r,c] + right[r,c]
        return s
    
    def __radd__(self, left):
        return self.__add__(left)
    
    def __sub__(self, right):
        if type(right) not in (int, float, Sparse_Matrix):
            raise TypeError("unsupported operand type(s) for +: '" + "Sparse_Matrix" + "' and '" + type_as_str(right) +"'")
        right = -right
        return self.__add__(right)
    
    def __rsub__(self, left):
        return type(self).__add__(-self, left)
    
    def __mul__(self, right):
        if type(right) not in (int, float, Sparse_Matrix):
            raise TypeError("unsupported operand type(s) for +: '" + "Sparse_Matrix" + "' and '" + type_as_str(right) +"'")
        elif type(right) in (int,float):
            m = Sparse_Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    m[r,c] = self[r,c]*right
            return m
        elif type(right) == Sparse_Matrix:
            assert self.rows == right.cols and self.cols == right.rows, "Two matrices cannot multiply."
            m = Sparse_Matrix(self.rows, right.cols)
            for r in range(m.rows):
                for c in range(m.cols):
                    m[r,c] = sum(x*y for x,y in zip(self.row(r), right.col(c)))
            return m
            
    def __rmul__(self, left):
        return self.__mul__(left)
    
    def __pow__(self, right):
        if type(right) != int:
            raise TypeError("unsupported operand type(s) for +: '" + "Sparse_Matrix" + "' and '" + type_as_str(right) +"'")
        assert right >= 1 and self.rows == self.cols
        return self if right == 1 else self*self.__pow__(right-1) 
    
    def __eq__(self, right):
        if type(right) not in (int, float, Sparse_Matrix):
            return False
        elif type(right) in (int,float):
            return all(right == self[r,c] for r in range(self.rows) for c in range(self.cols))
        elif type(right) == Sparse_Matrix:
            return self.rows == right.rows and self.cols == right.cols and all(x == y for x,y in zip(list(self.row(r) for r in range(self.rows)), list(right.row(r) for r in range(right.rows))))
    
    def __ne__(self, right):
        return not self.__eq__(right)
    
    def __setattr__(self, name, value):
        assert name not in self.__dict__ and name in ("rows", "cols", "matrix")
        self.__dict__[name] = value
        
    
if __name__ == '__main__':
    SM = Sparse_Matrix
    m1 = SM(2,3, (0,0,1),  (0,1,2), (0,2,3),  (1,0,4), (1,1,5),  (1,2,6))
    m2 = SM(2,3, (0,0,-1), (0,1,2), (0,2,-3), (1,0,4), (1,1,-5), (1,2,1))
    str(m1+m2)
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler

#     print('Printing')
#     m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
#     print(m)
#     print(repr(m))
#     print(m.details())
#   
#     print('\nlen and size')
#     print(len(m), m.size(),)
#     
#     print('\ngetitem and setitem')
#     print(m[1,1])
#     m[1,1] = 0
#     m[0,1] = 2
#     print(m.details())
# 
#     print('\niterator')
#     for r,c,v in m:
#         print((r,c),v)
#     
#     print('\nm, m+m, m+1, m==m, m==1')
#     print(m)
#     print(m+m)
#     print(m+1)
#     print(m==m)
#     print(m==1)
#     print()
    
    import driver
    driver.default_file_name = 'bscp22F20.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
