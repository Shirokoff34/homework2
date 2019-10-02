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

for replay in my_list[:3]:
    print(f'Номер повтора: {my_list[0:3]}')

print("--------------------------------------")

for printer in my_list[:3]:
    print(printer) 

#while True:



counter = 20

while counter > 4:
    counter = counter - 4
    print(counter)
else:
    print('Значение counter = ', counter)
