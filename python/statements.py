"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    # album = 'Revolver'
    # if album == 'Revolver':
    #     print('This is the album I like.')
    # elif album == 'Abbey Road':
    #     print('This is the album I like.')
    # else:
    #     print('That one is good as well.')

    # album1 = 'Revolver'
    # album2 = 'Revolver'
    # if album1 == album2:
    #     print('This is the album I like.')
    # else:
    #     print('That one is good as well.')
    # if album1 is album2:
    #     print('This is the album I like.')
    # else:
    #     print('That one is good as well.')

    from datetime import date
    # d1 = date(1966, 8, 5)
    # d2 = date(1966, 8, 5)
    # if d1 == d2:
    #     print('That\'s the date')
    # else:
    #     print('That\'s two different dates')

    # d1 = date(1966, 8, 5)
    # d2 = date(1966, 8, 5)
    # if d1 is d2:
    #     print('That\'s the date')
    # else:
    #     print('That\'s two different dates, address-wise')

    # if None:
    #     print('This is never printed')
    # else:
    #     print('This is printed when else is executed')

    if '':
        print('This is never printed')
    else:
        print('This is printed when else is executed')


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    for i in range(1, 10, 2):
        print(i)

    revolver = ['Revolver', 'The Beatles', 'UK']
    for i in revolver[1:]:
        print(i)

    for _ in range(4):
        print('Revolver')

    for i in range(10):
        if i == 3:
            continue
            # break
        print(i)

    i = 5
    while i:
        print(i)
        i -= 1


#%%
# Test demonstrate_loops()
demonstrate_loops()
