number_1 = int(input('Enter the metres value: '))
choice = int(input('Enter 1 to get miles value.\nEnter 2 to get inches value.\nEnter 3 to get yards value: \n'))

if choice == 1:
    print(f'The miles value is {number_1 / 1609.34}')
elif choice == 2:
    print(f'The inches value is {number_1 * 39.37}')
elif choice == 3:
    print(f'The yards value is {number_1 * 1.0936}')
else:
    print(f' Error, something is wrong with your choice')
