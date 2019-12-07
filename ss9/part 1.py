# items = ['red','blue','teal','yellow']
# print(items)
# print(*items)


# items = ['red','blue','teal','yellow']
# print('our colour list:')
# print(*items,sep=',')

items = ['red','blue','teal','yellow']
print('our colour list:')
print(*items,sep=',')
new_items = input('thêm màu bạn thích: ')
items.append(new_items)
print('our new colour list:')
print(*items,sep=',')