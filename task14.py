# Задача-14: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
answer = ''
while answer != 'нечётные':
    answer = input('чётные или нечётные ?: ')
    if answer == 'чётные':
        numbers = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        even = list(filter(lambda x: x % 2 == 0, numbers))
        print("Even numbers:", even)
if  answer == 'нечётные':
    numbers = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd = list(filter(lambda x: x % 2 != 0, numbers))
    oc = len(odd)
    print("Odd numbers:", odd)
#while True:
#    try:
#        if
#            break
#        else:
#            print('Некорректный ввод данных')
    #   except :
#       print("Ошибка")
