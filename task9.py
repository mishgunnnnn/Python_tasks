# Задание-9:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import re
line = 'mtMmEZUOmcq'
line_str = re.findall(r'[a-z]+', line)
print(line_str)
