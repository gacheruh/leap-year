year = int(input("Year: "))
if year % 4 == 0 and year% 100 != 0:
    print('true')
elif year % 400 == 0:
    print('true')
else:
    print('false')