number = int(input('value_1 ='))

part_1 = int(number/100)
print(part_1)
part_2 = int(number%100 / 10)
print(part_2)
part_3 = int(number%10)
print(part_3)
res = part_1 + part_2 + part_3
print(res)