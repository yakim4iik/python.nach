from random import *


def is_valid(n, ch1):
    if 1 <= n <= ch1:
        return True
    else:
        return False


def fun(num1, ch):
    count = 0
    while True:
        print('Введите вашу догадку:')
        n = int(input())
        count += 1
        if not is_valid(n, ch):
            print('А может быть все-таки введем целое число от 1 до', ch, '?')
        if n < num1:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num1:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == num1:
            print('Вы угадали, поздравляем!')
            print('Число попыток :', count)
            break


def snova():
    a = 'Да'
    while a == 'Да':
        print('Вы желаете сыграть еще раз?(Да/Нет)')
        a = input()
        if a == 'Да':
            print('Укажите границы от 1 до ?:')
            chislo1 = int(input())
            num1 = randint(1, chislo1)
            print('Число загадано')
            fun(num1, chislo1)


print('Добро пожаловать в числовую угадайку')
print('Укажите границы от 1 до ?:')
chislo = int(input())
num = randint(1, chislo)
print('Число загадано')
fun(num, chislo)
snova()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

