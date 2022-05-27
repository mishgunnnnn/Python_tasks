# Задача-6:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def condition(x):

    return x<30 and x>18

lst = [44, 23, 35, 0, 1, -17]

filtered = [x for x in lst if condition(x)]
print(filtered)
