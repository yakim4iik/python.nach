from random import *


def generate_password(n, lengt, ch):
    if n == 'Да':
        li = [choice(ch) for k in range(lengt) if choice(ch) not in 'il1Lo0O']
    else:
        li = [choice(ch) for k in range(lengt)]
    if len(li) != lengt:
        for k in range(lengt - len(li)):
            li.append(choice(ch))
    return print(*li, sep='')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
count_pass = int(input('Количество паролей для генерации?'))
length = int(input('Укажите длину одного пароля?'))
dig = input('Включать цифры?')
lower = input('Включать прописные буквы?')
upper = input('Включать заглавные буквы?')
pun = input('Включать символы?')
nes = input('Исключать ли неоднозначные символы?')
count = 0
chars = ''
if dig == 'Да':
    chars += digits
if lower == 'Да':
    chars += lowercase_letters
if upper == 'Да':
    chars += uppercase_letters
if pun == 'Да':
    chars += punctuation

for i in range(length):
    generate_password(nes, length, chars)
