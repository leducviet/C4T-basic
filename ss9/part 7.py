items = ('45','67','56','78')
a = ('điểm cao nhất:')
print(a,*items,sep=',')
for i,j in enumerate(items):
    print(i+1,j)
b = int(input('new high scores:'))
print(b)
