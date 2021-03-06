# Задание-5: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
while True:
    date = input('Введите дату формата dd.mm.yyyy: ')
    date = date.split('.')

    if len(date) == 3:
        if int(date[0]) < 1 or int(date[0]) > 31:
            print('Неверно указали день')
        elif int(date[1]) < 1 or int(date[1]) > 12:
            print('Неверно указали месяц')
        elif int(date[2]) < 1 or int(date[2]) > 9999:
            print('Неверно указали год')
        else:
            print('Формат даты корректный!')
            break
    else:
        print('Не правильный формат даты')
