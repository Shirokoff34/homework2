number_1 = 5

number_2 = 10

number_3 = None

if number_1 < number_2:
    print("Меньше")
else:
    print("Больше")

if number_3 is not None:
    print("Существует")
else:
    print("Не существует")

list_1 = list(range(1,11))

for a in [list_1]:
    if 15 in a:
        print("Есть")
    else:
        print("Нет в списке")

number_4 = 15

number_5 = 16

if number_5 > number_1:
    print("Меньше первого")
elif number_5 > number_2:
    print("Меньше второго")
elif number_5 > number_4:
    print("Меньше четвертого")
else:
    print("Больше всех")