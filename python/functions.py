"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Taxman'
year = 1966

john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]


#%%
# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    # print(title + ': ' + str(year))
    print(f'{title}: {year}')
    print(demonstrate_annotations.__annotations__)
    print(f'{demonstrate_annotations.__name__}(\'{title}\', {year}): \n{demonstrate_annotations.__doc__}')
    return f'demonstrate_annotations(\'{title}\', {year})'


#%%
# Test demonstrate_annotations(title, year)
demonstrate_annotations(song, year)


#%%
def show_song(title, author=george, year: int = 1968):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())

    print(f'{title} by {author} ({year})')


#%%
# Test def show_song(title, author=george, year: int = 1966):
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # print(members)
    # print(*members)

    print(f'{band}: {", ".join(m for m in members)}' if members else band)


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Beatles', *the_beatles)
use_flexible_arg_list('The Beatles')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    # print(details)
    # print(*details)
    # # print(**details)

    b = band
    m = ', '.join(m for m in members) if members else ''
    a = 'active' if is_active else 'inactive'
    d = ', '.join([str(k) + ": " + str(v) for k, v in details.items()] if details else '')

    if m and d:
        print(f'{b}: {m} ({a}), {d}')
    elif m:
        print(f'{b}: {m} ({a})')
    elif d:
        print(f'{b} ({a}), {d}')
    else:
        print(f'{b} ({a})')


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
use_all_categories_of_args('The Beatles', *the_beatles, is_active=False,
                           start=1962, end=1970)
