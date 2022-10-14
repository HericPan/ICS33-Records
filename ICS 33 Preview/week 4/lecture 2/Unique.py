from collections import defaultdict  
class Unique:
    def __init__(self, iterable, max_times=1):
        self._iterable  = iterable
        self._max_times = max_times
        
    def __iter__(self):
        class Unique_iter:
            def __init__(self, iterable, max_times):
                self._times     = defaultdict(int)
                self._iterator  = iter(iterable)
                self._max_times = max_times
            
            def __next__(self):
                answer = next(self._iterator)        # StopIteration raised?
                while self._times[answer] >= self._max_times:
                    answer = next(self._iterator)       # StopIteration raised?
                self._times[answer] += 1
                return answer

            def __iter__(self):
                return self

        return Unique_iter(self._iterable, self._max_times)
