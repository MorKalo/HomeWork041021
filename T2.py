i=0
_sum=0
num=int(input('Plz insert a number'))
while num!=0:
    if num>77:
       i=i+1
       _sum=_sum+num
    num=int(input('Plz insert a number'))
print ('you enterd', i,'numbers that bigger then 77')
print('the sum of the numbers that bigger then 77 is', _sum )