# Задание-8:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
km = int(input('введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print('Кол-во миль: ', miles)
convert(km)
