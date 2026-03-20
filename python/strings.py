"""Demonstrates working with strings in Python.
"""


#%%
def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    album = 'Revolver'
    band = 'The Beatles'
    year = 1966
    print(f'The album {album} was released in {year} by {band}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    album = 'Revolver'
    # album[2] = 'X'                      # No! Strings are immutable
    print(album)
    print(album.endswith('l'))
    print(album.split('l'))
    print(album.center(20, '-'))
    print('Rev' in album)
    print(album == 'The Beatles')
    print(len(album))

    album = '           Revolver '
    print(album)
    print(album.strip())
    print(album.lstrip() + 'd')


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
