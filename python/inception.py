"""The very first module in a more structured version of the project.
"""


#%%
# # Moving part of the code from main.py
# print('Revolver')

#%%
# # Printing with ' ' and printing without '\n'
# print('Revolver', 'The Beatles', 'UK', sep=' ')

#%%
# A simple function and function call
def album_title(title):
    """Prints the title of the album."""
    print(f'The album title is {title}.')

# album_title('Revolver')
# print(album_title('Revolver'))
#
# print(__name__)

#%%
# # Printing docstrings
# print(revolver_title.__doc__)
# print(__doc__)

#%%
# # break and continue
# for i in range(1, 5):
#     if i == 3:
#         continue
#         # break
#     print(i)

#%%
# Importing from Standard Library

# # Date format strings
# # https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes
# from datetime import date
# d = date(1966, 8, 5)
# print(d)

#%%
# Testing print(__file__)


#%%
# Taking care of the module __name__
if __name__ == '__main__':
    print('Revolver')
    print()

    album_title('Revolver')
    print(album_title('Revolver'))
    print()

    print(album_title.__doc__)
    print(__doc__)
    print()

    for i in range(1, 5):
        if i == 3:
            continue
            # break
        print(i)
    print()

    from datetime import date
    d = date(1966, 8, 5)
    print(d)

    print(__name__)


