items = ('st','BD','BTL','CG','DD','HBT')
a = ('thứ tự các quận trong thành phố:')
print(a,*items,sep=',')
number = ('150,300','247,100','333,300','266,800','420,900','318,000')
b = ('số dân theo thứ tự các quận:')
print(b,*number,sep=';')
smallest = ('st')
c = ('quận có số dân ít nhất:')
print(*c,*smallest,sep='')
print('150,300')
biggest = ('DD')
c = ('quận có số dân nhiều nhất:')
print(*c,*biggest,sep='')
print('420,900')



