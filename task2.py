# Задача-2:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
lst1 = [2, -5, 9, 25, 36, 31, 0]
lst2 = []
for result in lst1:
    if result > 0:
        result = result ** .5
        if result % 1 == 0:
            result = int(result)
            lst2.append(result)
print(lst2)
