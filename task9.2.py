# Задание-9:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcq'

symbol = list(map(lambda x: chr(x), list(range(65, 91))))
line_new = list(line)

for i, element in enumerate(line_new[:]):
    for element_2 in symbol:
        if element == element_2:
            line_new[i] = ' '

linia = ''.join(line_new).split(' ')

line_str_2 = [i for i in linia if i != '']
print(line_str_2)
