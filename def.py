# Напиши функцию do_notning, которая не принимает аргументов и ничего не делает
def do_nothing():
    print('Do nothing')

# Напиши функцию my_print, которая принимает один обязательный параметр и печатает его
def my_print(A):
    return(A)
A = [1, 2, 3, 4]
print(A)

print('-------------------')

# Напиши функцию print_hello, которая принимает на вход Имя человека и печатает "Hello, имя!"
name = input('Whats your name: ')
print('Hello', name)
# Использовал встроенную функцию input

print('-------------------')

# Напиши функцию с двумя именными аргументами, которая печатает эти два аргумента
# Сделай вызов этой функции, передав аргументы в обратном порядке (в описании функции а и б, в вызове б а)
def print_argum(a, b):
    print (a, b)
print_argum(b = 10, a = 5)

print('-------------------')

# Напиши функцию, которая возвращает результат сложения двух аргументов, которые в нее передали.
# Напечатай результат работы функции
def print_argum(a, b):
    return a + b
result = print_argum(2, 4)
print(result)
# Сделал через return хотя можно сделать и через print внутри функции?

print('-------------------')

# Напиши функцию, которая принимает два аргумента: строку и опционально число, по умолчанию 20
# Функция проверяет, если длина строки более этого числа, то обрезает ее и ставит ... в конце. Функция возвращает результат,
# сохраняем его в переменную, результат печатаем
def two_arg(a, b=20):
    a = str(a)
    if len(a) > b:
         a = a[:19] + "..."
    else:
        return(a)
    return(a)
result = two_arg(a = "LearnPythonLearnPythonLearnPythonLearnPythonLearnPythonLearnPython")
print(result)
# Мне кажется все равно кривовато

print('-------------------')

# Функция принимает на вход полные Фамилия Имя Отчество и возвращает Фамилия И.О.
def name_fio(name, lastname, patronymic):
    name = str(name)
    lastname = str(lastname)
    patronymic = str(patronymic)
    print(name + f' {lastname[0]}.' + f' {patronymic[0]}.')

name_fio(name = 'Широков', lastname = 'Дмитрий', patronymic = 'Валерьевич')

print('-------------------')

# Функиця принимает на вход строку и проверяет, есть ли в ней гласные.
# Если есть - посчитать сколько их и вернуть результат, сколько и каких гласных есть
def search_vowels(word):
    word = str(word)
    vowels = 0
    for letter in word:
        if letter.lower() in "aeyuio":
            vowels += 1
    vowels_2 = set('aeyuio')
    founder = vowels_2.intersection(set(word))
    for vowel in founder:
        print(vowel)
    return print(vowels)

search_vowels(word = input("Enter the word: "))

# Криво, но работает