def function_cycler(func1, *funcs): # func1 here makes it mandatory to give at least one functions
    funcs = [func1] + list(funcs) # concatenate and convert the first function and 2+nd function tuple
    # Here use closure variable to keep track of the count times.
    times_called = [0]
    print(funcs)
    def internal_func(n):
        
        # Reminder! nth call refer to nth function in the (n-1)th index!
        # if calling the n+1th, we will call the 1st function again...
        # thus we have to use % mod operator and len() to calculate the current index!
        # current index: (current_counts) % len(funcs) - 1
        times_called[0] += 1
        current_index = times_called[0] % len(funcs) - 1
        
        # Calling the function formally
        return funcs[current_index](n)
    return internal_func

cycler = function_cycler((lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
print(cycler(1))
print(cycler(2))
print(cycler(3))
print(cycler(10))
print(cycler(11))