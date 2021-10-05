#לבקשת איתי שימוש ב10 קלטים במקוםל 1000
i=1
_sum=int(input('insert a ticket'))
while i<=9:
    ticket = int(input('insert a ticket'))
    if _sum == ticket:
        print('The number', ticket, 'is equal to the sum of all its predecessors')#המספר שהכנסת שווה לסכום כל קודמיו
        break
    _sum = _sum + ticket
    i=i+1
if i==10:
    print ('NOT FOUND')