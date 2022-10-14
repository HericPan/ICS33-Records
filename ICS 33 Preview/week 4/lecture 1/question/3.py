def first(something, func : callable):
    i = iter(something)
    first = next(i)
    if func(first): 
        return first
    else:
        try:
            while True:
                if func(next(i)): return "HAHA, the others might True"
        except StopIteration:
            raise ValueError
        

print(first([1,2,3,4,5], (lambda x: x == 100)))