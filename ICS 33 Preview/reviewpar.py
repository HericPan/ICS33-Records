import builtins

del builtins.print
print(9)

del print
print(10)

builtins.print = original_print