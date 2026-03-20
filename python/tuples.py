"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    t0 = ()
    print(t0)
    print(type(t0))
    print()

    t1 = 'Revolver',
    print(t1)
    print()

    t2 = 'Revolver', 1966
    print(t2)
    print()

    t3 = 'Revolver', 1966, True
    print(t3)
    print()

    print(t3[0])
    print(t3[1:])
    print(t3[-1])
    print()

    # t3[0] = 'The Beatles'           # No! Tuples are immutable


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """
    t3 = 'Revolver', 1966, True
    revolver, year, is_great = t3
    print(f'The album {revolver} was released in {year}.')

#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr', )
    birth_years = (1940, 1942, 1943, 1940)
    birth_places = ('Liverpool', 'Liverpool', 'Liverpool', 'Liverpool' )

    print(zip(members, birth_years, birth_places))
    print(list(zip(members, birth_years, birth_places)))
    print()

    for member, birth_year, birth_place in zip(members, birth_years, birth_places):
        print(f'{member} was born in {birth_year} in {birth_place}.')
    print()

    the_beatles_zip = zip(members, birth_years, birth_places)
    print(the_beatles_zip)
    print(list(the_beatles_zip))

    # print(next(the_beatles_zip))        # No! The zip is exhausted


#%%
# Test demonstrate_zip
demonstrate_zip()

