number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
choice = int(input('Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for Multiplication.\nEnter 4 for '
                   'arithmetical mean: \n'))

if choice == 1:
    print(f'The sum is {number_1 + number_2}')
elif choice == 2:
    print(f'The sum of subtraction is {number_1 - number_2}')
elif choice == 3:
    print(f' The sum of multiplication is {number_1 * number_2}')
elif choice == 4:
    print(f' The arithmetical mean is {(number_1 + number_2) // 2}')
else:
    print(f' Error, something is wrong with your choice')