def transform_alabo2_roman_num(one_num):
   
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res=''
    for i in range(len(num_list)):
        while one_num>=num_list[i]:
            one_num-=num_list[i]
            res+=str_list[i]
    return res



class Counter:                   # implicitly use object as its base class
    hierarchy_depth = 1         # object is at depth 0, Counter is 1 beneath it
    counter_base = 0           # track how often Counter.__init__ is called

    def __init__(self,init_value=0):
        assert init_value >= 0,\
            'Counter.__init__ init_value('+str(init_value)+') < 0'
        self._value = init_value
        Counter.counter_base += 1    # Increment class variable on __init__ call

    def __str__(self):               # str of Counter is str of its _value
        return str(self._value)
        
    def reset(self):                 # reset of Counter assigns _value = 0
        self._value = 0
        
    def inc(self):                   # inc(rement) of Counter increments _value
        self._value += 1
        
    def value_of(self):              # value_of Counter is _value (an int)
        return self._value
    
    def print_it(self):
        print(str(self))
    

class Modular_Counter(Counter): # explicitly use Counter as its base class
    hierarchy_depth = Counter.hierarchy_depth + 1 # 1 more than Counter's depth
    counter_derived = 0         # how many times Modular_Counter.__init__ called

    def __init__(self,init_value,modulus):
        assert modulus >= 1,\
            'Modular_Counter.__init__ modulus('+str(init_value)+') < 1'
        assert 0 <= init_value < modulus,\
            'Modular_Counter.__init__ init_value('+str(init_value)+') not in [0,'+str(modulus)+')'
        Counter.__init__(self,init_value)
        self._modulus = modulus
        Modular_Counter.counter_derived += 1    
    
    def __str__(self):
        return Counter.__str__(self)+' mod '+str(self._modulus)
        
    # Note, calling self.value_of() and self.reset() is equivalent to (and
    #   preferred to) calling Counter.value_of(self) and Counter.reset(self)
    # But it is critical that Counter.inc(self) is called that way, because
    #   calling self.inc() would be an infinitely recursive call to inc.
    def inc(self):
        if self.value_of() == self._modulus - 1:
            self.reset()
        else:
            Counter.inc(self)
        
    def modulus_of(self):
        return self._modulus
    def print_it(self):
        print(str(self))

if __name__ == '__main__':
    import prompt

    c = Counter(0)
    mc = Modular_Counter(0,3)

    while True:
        try:
            exec(prompt.for_string('Command'))
        except Exception as report:
            import traceback
            traceback.print_exc()