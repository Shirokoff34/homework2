my_list = list(range(1,11))

print(my_list)

for i in my_list:
    i = i + 1
    print(i)

print("--------------------------")

for i in my_list:
    i = i - 1
    print(i)

print('--------------------------')

for replay in my_list:
    print(f'Номер повтора: {my_list[0:3]}')