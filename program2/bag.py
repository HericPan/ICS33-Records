# Submitter: ruohuaip(Pan, Ruohuai)
# Partner  : haoyuaz9(Zhang, haoyuan)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from collections import defaultdict
from goody       import type_as_str
import prompt

class Bag:
    def __init__(self, l=[]):
        self._bagdict = defaultdict(int)
        for x in l: self._bagdict[x] += 1
    
    def __repr__(self):
        record = list()
        for k in self._bagdict:
            for _ in range(self._bagdict[k]):
                record.append(k)
        return f'Bag({record})'

    def __str__(self):
        return "Bag(" + ", ".join(f"{k}[{self._bagdict[k]}]" for k in self._bagdict) + ")"
    
    
    def __len__(self):
        return sum(v for v in self._bagdict.values())
    
    
    def unique(self):
        return len(self._bagdict)

    def __contains__(self, key):
        return key in self._bagdict
    
    def count(self, item):
        return self._bagdict[item] if item in self._bagdict else 0
    
    def add(self, item):
        self._bagdict[item] += 1
        
    def __add__(self, nb):
        if type(nb) != Bag: raise TypeError("The right value is not Bag.")
        b = Bag()
        for k in self._bagdict:
            for _ in range(self._bagdict[k]):
                b.add(k)
        for k in nb._bagdict:
            for _ in range(nb._bagdict[k]):
                b.add(k)
        return b
    
    def remove(self, item):
        if item in self._bagdict:
            if self._bagdict[item] == 1:
                self._bagdict.pop(item)
            else:
                self._bagdict[item] -= 1
        else:
            raise ValueError(f"Value {item} is not in the dictionary.")
    
    def __eq__(self, b2):
        if type(b2) != Bag: return False
        return self._bagdict == b2._bagdict
    
    def __ne__(self, b2):
        if type(b2) != Bag: return True
        return self._bagdict != b2._bagdict
    
    def __iter__(self):
        class Bag_iterator:
            def __init__(self, d):
                self.l = list()
                for k in d:
                    for _ in range(d[k]):
                        self.l.append(k)
            
            def __next__(self):
                if len(self.l) != 0:
                    return self.l.pop(0)
                else:
                    raise StopIteration
            
            def __iter__(self):
                return self
        return Bag_iterator(self._bagdict)

if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)
 
    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21F20.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
