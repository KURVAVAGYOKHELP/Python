number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))
choice = int(input('Enter 1 for addition.\nEnter 2 for multiplication:\n '))

if choice == 1:
    print(f'The sum is {number_1 + number_2 + number_3}')
elif choice == 2:
    print(f'The sum of subtraction is {number_1 * number_2 * number_3}')
else:
    print(f' Error, something is wrong with your choice')