"""The very first Python script - main.py.
"""


#%%
# # Hello world: the print() built-in function and the + operator.
# print('Revolver')
# print('Revolver' + ', The Beatles')
#
#
# #%%
# # The input() built-in function
# revolver = input('The album title: ')
# print(f'The album title is {revolver}.')
#
#
# #%%
# # A simple function and function call
# def album_title(title):
#     """Prints the title of the album."""
#     print(f'The album title is {title}.')
#
# album_title('Revolver')
# print(album_title('Revolver'))
#
#
# #%%
# # A simple loop and the range() built-in function
# for i in range(1, 5):
#     print(i)
#
#
# #%%
# # A simple list, accessing list elements, printing lists
# revolver = ['Revolver', 'The Beatles', 'UK']
# print(revolver[0])
# print(revolver)
# for i in revolver:
#     print(i)
#
#
# #%%
# # Looping through list elements - for and enumerate()
# for i, j in enumerate(revolver):
#     print(f'{i+1}: {j}')
#
#
# #%%
# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# print(__file__)


#%%
# Importing from another script
from inception import album_title
album_title('Revolver')


