no1=int(input('Enter First Number '))
no2=int(input('Enter Second Number '))
no3=int(input('Enter Third Number '))

if no1>no2 and no1>no3:
    print('First Number : = '+str(no1)+ ' is greater')
elif no2>no1 and no2>no3:
    print('Second Number : = '+str(no2) + ' is greater')
else:
    print('Third Number : = '+str(no3) +' is greater')

