"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    revolver = ['Revolver', 'The Beatles', 1966]
    the_beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr', ]
    years = [1962, 1966, 1970, 1973, 1977, 1981, 1985, 1989, 1993, 1997, ]

    print(revolver)
    print(the_beatles[0])
    print(years[2:5])
    print(years[-1])
    print(years[2:-1])
    print(years[2:])
    print()

    print(revolver == ['Revolver', 'The Beatles', 1966])
    print(revolver is ['Revolver', 'The Beatles', 1966])
    print()

    print(the_beatles + years)
    print()

    for i in years:
        print(i)


#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    the_beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr', ]
    the_beatles.append('Liverpool')
    print(the_beatles)
    the_beatles.insert(2, 'George Martin')
    print(the_beatles)
    the_beatles.remove('George Martin')
    print(the_beatles)
    the_beatles.pop()
    print(the_beatles)
    the_beatles.extend(['George Martin', 'Brian Epstein'])
    print(the_beatles)
    print(the_beatles.count('George Martin'))
    print(the_beatles.index('Ringo Starr'))
    the_beatles.reverse()
    print(the_beatles)
    print(len(the_beatles))
    print('Ringo' in the_beatles)
    print('Ringo' not in the_beatles)


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import seed, randint
    l = []
    seed(1)
    for i in range(10):
        l.append(randint(0, 100))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """
    l1 = [1, 2, 3, 4, 5]
    # l2 = l1
    # print(l1 is l2)
    # l2 = l1.copy()
    # l2 = l1 + []
    l2 = l1[:]
    print(l1 is l2)


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane', ]

    first_words = [title.split()[0] for title in songs]
    print(first_words)
    first_letters = [w[0] for w in first_words]
    print(first_letters)
    print(''.join(first_letters).capitalize() + '!')

    print(''.join([title.split()[0][0] for title in songs]).capitalize() + '!')
    print()

    songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane',
             'Eleanor Rigby', 'Lucy in the Sky With Diamonds', ]

    print(', '.join([title for title in songs if not songs.count(title) > 1]))
    print(', '.join([title for title in set(songs)]))
    print(', '.join([str(i) for i, j in enumerate(songs) if songs.count(j) > 1]))


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

