# a = int(input('Введите число: '))
# b = input('Введите знак: ')
# c = int(input('Введите число: '))
# try:
#     if b == '+':
#         print(f'{a} + {c} = {a + c} ')
#     elif b == '-':
#         print(f'{a} - {c} = {a - c} ')
#     elif b == '*':
#         print(f'{a} * {c} = {a * c} ')
#     elif b == '/':
#         print(f'{a} / {c} = {a / c} ')
# except ZeroDivisionError:
#     print('Ошибка деления на 0')
#     print(f'{a ** 2} ')

def sloj(a, c):
    total = a + c
    print(total)


def otnim(a, c):
    total = a - c
    print(total)


def umnoj(a, c):
    total = a * c
    print(total)


def delen(a, c):
    total = a / c
    print(total)
    print("Возведение в квадрат:", total**2)


def calculator(a, c):
    try:
        if znak == '+':
            sloj(a, c)
        elif znak == '-':
            otnim(a, c)
        elif znak == '*':
            umnoj(a, c)
        elif znak == '/':
            delen(a, c)
    except ZeroDivisionError:
        print(f'Ошибка деления на 0. Так делать нельзя!')
    finally:
        print("Программа отработала")


a = int(input('Введите число: '))
znak = input('Введите знак"+,-,*,/": ')
c = int(input('Введите число: '))
calculator(a, c)

### Домашнее задание № 1 ###
def chislo():
    while True:
        text = input('Введите 2 числа: ')   # создаю цикл с запросом числел для повторного запроса чисел если второе число будет 0
        new_text = text.split()             # разбиваю строку на подстроки, чтобы можно было выполнить арифмет. действие
        if len(new_text) == 2:              # создаем условие для продолжения выполнения арифм. действия
            try:
                c = int(new_text[0]) / int(new_text[1])     # выполняем деление одного числа на другое.
                print(c)
                break                       # останавливаем цикл при корректном выполнении задачи
            except ZeroDivisionError:       # обработка ошибки при делении на "0" и программа повторно запрашивает ввести данные
                print('Делить на 0 нельзя! Повторите еще раз!')
            except ValueError:              # обработка ошибки на ввод букв.
                print('Вы ввели буквы вместо чисел. Попробуйте повторить запрос')


chislo()
