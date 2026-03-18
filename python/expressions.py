"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    return 2 + 33 // 4 - (18 - 2)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    # print(2 > 3)
    # print(3 == 3)

    from datetime import date
    d1 = date.today()
    d2 = date(1957, 7, 6)
    d3 = date.today()
    # print(d1 == d2)
    # print(d1 == d3)
    # print(d1 is d3)
    # print(d1 > d2)

    # print(id(d1))
    # print(id(d3))

    # a = 1
    # b = 1
    # a = 'Revolver'
    # b = 'Revolver'
    # print(a == b)
    # print(a is b)

    # print(type(None))
    # print(None > 2)
    print(None != 2)


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()


#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    # print((1 > 2) and (4 < 5))
    # print((1 > 2) or (4 < 5))

    from datetime import date
    d1 = date.today()
    d2 = date(1957, 7, 6)
    d3 = date.today()
    # print(d1 and d2)
    print(None or d2)
    print(None or 0)
    print(None > d2)

#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

