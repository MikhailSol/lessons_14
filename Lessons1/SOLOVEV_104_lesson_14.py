import os
f = open('example.txt', 'r')
f = open('test.txt', 'r')
print(f.readline())
print(f.readlines())

### Задание № 1 ####
f = open('test.txt', 'r')
new_f = f.read()
print(new_f)
total = 0
for i in new_f:
    if i.isdigit():
        total = total + int(i)
print(total)

### Задание № 2 ####
f = open('test.txt', 'r')
new_f = f.read()
new_list =[]
new_list_1 = []
for i in new_f.split('\n'):
    if i.isdigit():
        new_list.append(i)
    else:
        new_list_1.append(i)
new_str = new_list + new_list_1
print(sorted(new_list) + sorted(new_list_1))

### Задание № 3 ####
f = open('new_progect.txt', 'w')    #если нету такого файла с именем, то создает автоматически его(у меня создался)
while True:                         # задаем цикл для ввода информации
    text = input('Введите данные(для завершегия работы укажите" "): ')
    if text != ' ':                 # задаем условие для работы цикла
        f.write(text + '\n')        # согласно условию ввод с новой строки
    else:
        break
print('Программа завершена')
f.close()

### Задание № 4 ####
new_line = 0
f = open('new_progect.txt', 'r')
for i in f:
    new_line = new_line + 1
    print(len(i) -1, ':символов')
    print(i)
print('Количество строк:', new_line)

### Домашнее задание № 1 ####
f = open('new_progect.txt', 'w')
arr = [5, 9, 3, 2, 4, 'Hello', 'hi', 'good', 'by']
new_int = []
new_str = []
for i in arr:
    if i == str(i):
        new_str.append(i)
        new_str.sort(key=len)
    else:
        new_int.append(i)
new_str.extend(sorted(new_int))
print(new_str)

### Домашнее задание № 2 ####
f_n = open('Project_lessons.txt', 'w')
while True:
    upfile = input("Введите число или текст: ")
    if upfile == '0':
        break
    f_n.write(upfile + '\n')
print('Ввод данных завершен')
f_n.close()

f_n = open('Project_lessons.txt', 'r')
new_f = f_n.read()
spis_int = []
spis_str = []
for i in new_f.split('\n'):
    if i.isdigit():
        spis_int.append(i)
        spis_int.sort()
    else:
        spis_str.append(i)
        spis_str.sort(key=len)
spis_int.extend(spis_str)
spis_int.remove('')
print(spis_int)
os.rename('Lesson_13.py', 'SOLOVEV_104_lesson_14.py')