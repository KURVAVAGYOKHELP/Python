number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))
choice = int(input('Enter 1 for the maximum number.\nEnter 2 for the minimum number.\nEnter 3 for the arithmetical'
                   'mean:\n '))

if choice == 1:
    if number_1 > number_2 and number_1 > number_3:
        print('%.d is the maximum number'
              %(number_1))
    elif number_2 > number_3 and number_2 > number_3:
        print('%.d is the maximum number'
              %(number_2))
    elif number_3 > number_1 and number_3 > number_2:
        print('%.d is the maximum number'
              %(number_3))
elif choice == 2:
    if number_1 < number_2 and number_1 < number_3:
        print('%.d is the minimum number'
              %(number_1))
    elif number_2 < number_3 and number_2 < number_3:
        print('%.d is the minimum number'
              %(number_2))
    elif number_3 < number_1 and number_3 < number_2:
        print('%.d is the minimum number'
              %(number_3))
elif choice == 3:
    print(f'The arithmetical mean is {(number_1 + number_2 + number_3) // 3}')
else:
    print(f' Error, something is wrong with your choice')
