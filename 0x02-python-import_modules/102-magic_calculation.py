#!/usr/bin/python3

def magic_calculation(a, b):
    """Diassembly python bytecode."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(3, 10):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
