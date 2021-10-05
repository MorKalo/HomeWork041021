#לבקשת איתי שימוש ב10 קלטים בלבד
yes=0
no=0
avoid=0
veto=0
i=0
while i<=9:
    choice=int(input('plz insert youre choice, 1 for YES; 2 for NO; 3 for AVOID; 4 for VETO'))
    i=i+1
    if choice==4:
        print('the The serial number of the country is', i)
        break
    elif choice==1:
        yes=yes+1
    elif choice==2:
        no=no+1
    elif choice==3:
        avoid=avoid+1
print('the number of Supporte:', yes)
print('the number of aggainst:', no)
print('the number of avoid:', avoid)
