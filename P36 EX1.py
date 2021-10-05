#לבקשת איתי שימוש ב10 מספרים בלבד במקום 100
i=1
first=int(input('Plz insert a number'))
while i<=9:
    second=int(input('Plz insert another number'))
    if second<first:
        print('The numbers are NOT sorted')
        break
    first = second
    i=i+1
if i==10:
    print ('The numbers are  sorted')