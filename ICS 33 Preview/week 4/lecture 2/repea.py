class Repeat:
    def __init__(self, iterable, max_times=None):
        self._iterable  = iterable
        self._max_times = max_times
        
    def __iter__(self):
        class Repeat_iter:
            def __init__(self, iterable, max_times):
                self._iterable       = iterable
                self._max_times_left = max_times
                self._iterator       = iter(iterable)
            
            def __next__(self):
                if self._max_times_left != None and self._max_times_left <= 0:
                    raise StopIteration
                else:
                    try:
                        return next(self._iterator)     # StopIteration raised?
                    except StopIteration:
                        if self._max_times_left != None:
                            self._max_times_left -= 1 
                        self._iterator = iter(self._iterable)
                        return next(self)        # StopIteration raised?

            def __iter__(self):
                return self

        return Repeat_iter(self._iterable, self._max_times)