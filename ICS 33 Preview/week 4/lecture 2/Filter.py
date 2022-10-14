class Filter:
    def __init__(self, iterable, predicate):
        self._iterable = iterable
        self._predicate = predicate
    
    def __iter__(self):
        class Filter_iter:
            def __init__(self,iterable, predicate):
                self._iterator = iter(iterable)
                self._predicate = predicate
            
            def __next__(self):
                answer = next(self._iterator)
                while self._predicate(answer) == False:
                    answer = next(self._iterator)
                return answer
            
            def __iter__(self):
                return self
        return Filter_iter(self._iterable, self._predicate)