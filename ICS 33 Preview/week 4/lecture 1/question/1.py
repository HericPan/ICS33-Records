_hidden = iter(iterable)        # ultimately calls iterable.__iter__()
try:
    while True:
        index(es) = next(_hidden)    # ultimatelyl calls _hidden.__next__()
        block-body
except StopIteration:
    pass                # A place-holder, when [] is discarded;
    [block-else]            #    the except block cannot be empty
finally:
  del _hidden                # Remove _hidden from name_space