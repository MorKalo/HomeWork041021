#לבקשת איתי שימוש בקליטת 10 כרטיסים בלבד
i=1
tmax=40
tmin=-5
while i<=9:
    ticket = int(input('insert the temp'))
    if tmin>ticket or ticket>=tmax:
        print('WRONG value')
        break
    i=i+1
if i==10:
  print ('GOOD value')