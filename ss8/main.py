# items = ['com','chao','pho']
# print(items)
# new_items = input('món mới:')
# items.append(new_items)
# print(items)
# items = (items+new_items)


# colours = ['blue', 'green', 'yellow','Dark', 'white']

# while len(colours) != 0:
#     option = input('Enter name or index of item you want to delete: ')
#     if option.isdigit():
#         print('Pop ',option,' (',colours[int(option)],')')
#         colours.pop(int(option))
#     elif option.isalpha():
#         isIn = False
#         for i in colours:
#             if i == option:
#                 colours.remove(i)
#                 print('Remove ',option)
#                 isIn = True
#                 break
#         if isIn == False:
#             print('Not Found Item ',option)
#     else:
#         print('Wrong input!!!')
#     print(colours)