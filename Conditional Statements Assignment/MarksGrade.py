marks = int(input('Enter Marks'))

if marks>=80:
    print('Distinction')
elif marks>=70 and marks<80:
    print('First Class')
elif marks>=60 and marks<70:
    print('Second Class')
elif marks>=50 and marks<60:
    print('Pass')
else:
    print('Fail')
