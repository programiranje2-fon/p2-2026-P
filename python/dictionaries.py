"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # d0 = {}
    # print(type(d0))
    # print()

    songs = {'Yellow Submarine': 3, 'Dr. Robert': 1, 'Tomorrow Never Knows': 2}
    # print(type(songs))
    # print()
    #
    # print(songs['Yellow Submarine'])
    # print(songs['Tomorrow Never Knows'])
    # print()

    # print(songs.items())
    # print()
    #
    # for k, v in songs.items():
    #     print(k+':', v)
    # print()

    songs['She Said She Said'] = 8
    print(songs)
    print()

    del songs['Tomorrow Never Knows']
    print(songs)
    print()

    # songs.update({'I\'m Only Sleeping': 4})
    songs.update([('I\'m Only Sleeping', 4)])
    print(songs)
    print()

    print(songs.keys())
    print()

    print(songs.values())


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter
    # if by == 'k' or by == 'K':
    #     # return dict(sorted(d.items(), key=itemgetter(0)))
    #     return {k:v for k, v in sorted(d.items(), key=itemgetter(0))}
    # elif by == 'v' or by == 'V':
    #     # return dict(sorted(d.items(), key=itemgetter(1)))
    #     return {k:v for k, v in sorted(d.items(), key=itemgetter(1))}
    # else:
    #     return None

    if by == 'k' or by == 'K':
        return dict(sorted(d.items(), key=lambda x: x[0]))
    elif by == 'v' or by == 'V':
        return dict(sorted(d.items(), key=lambda x: x[1]))
    else:
        return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    # from pprint import pprint         # when sorting by values, pprint doesn't show the resulting dictionary correctly

    songs = {3: 'Yellow Submarine', 1: 'Dr. Robert', 2: 'I\'m Only Sleeping', 8: 'She Said She Said'}
    # the_beatles = {'place': 'Liverpool', 'name': 'The Beatles', 'year': 1962}
    the_beatles = {'place': 'Liverpool', 'name': 'The Beatles', 'year': '1962'}

    print(sort_dictionary(songs, 'k'))
    print(sort_dictionary(songs, 'v'))
    print(sort_dictionary(the_beatles, 'k'))
    print(sort_dictionary(the_beatles, 'v'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()


#%%
def dict_comprehension(l1, l2):
    """
    Demonstrate dict comprehension
    :param l1: a list (or another iterable) of dict keys
    :param l2: a list (or another iterable) of dict values
    :return: a dict created by dict comprehension
    """

    return {k:v for k, v in zip(l1, l2)}


#%%
# Test dict_comprehension(l1, l2)
print(dict_comprehension(['rhythm guitar', 'bass', 'lead guitar', 'drums'],
                         ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']))
