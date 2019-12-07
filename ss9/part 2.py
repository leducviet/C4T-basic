# items = ['red','blue','teal','yellow']
# i =int(input("enter position: "))
# a = ('colour at position',[i])
# print(*a,sep=':')
# print(items[i])



items = ['red','blue','teal','yellow']
i = input('')
if i.isdigit():
    items.pop(int(i)-1)
    print(items)
elif i.isalpha:
    items.remove(i)
    print(items)