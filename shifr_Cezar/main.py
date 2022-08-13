
def shifr(lang, sdvig, s1):

    li = []
    if lang == 'ру':
        for i in range(len(s1)):
            if s1[i] in '.,?!"' or s1[i] == ' ':
                li.append(s1[i])
                continue
            if s1[i] == s1[i].upper():
                n = ord(s1[i]) + sdvig
                if n > 1071:
                    n -= 32
                li.append(chr(n))
            else:
                n = ord(s1[i]) + sdvig
                if n > 1103:
                    n -= 32
                li.append(chr(n))
        return print(*li, sep='')
    elif lang == 'ан':
        for i in range(len(s1)):
            if s1[i] in '.,?!"' or s1[i] == ' ':
                li.append(s1[i])
                continue
            if s1[i] == s1[i].upper():
                n = ord(s1[i]) + sdvig
                if n > 90:
                    n -= 26
                li.append(chr(n))
            else:
                n = ord(s1[i]) + sdvig
                if n > 122:
                    n -= 26
                li.append(chr(n))
        return print(*li, sep='')
    else:
        return print('我不懂這種語言')


def deshifr(lang, sdvig, s1):
    li = []
    if lang == 'ру':
        for i in range(len(s1)):
            if s1[i] in '.,?!" ' or s1[i] == ' ':
                li.append(s1[i])
                continue
            if s1[i] == s1[i].upper():
                n = ord(s1[i]) - sdvig
                if n < 1040:
                    n += 32
                li.append(chr(n))
            else:
                n = ord(s1[i]) - sdvig
                if n < 1072:
                    n += 32
                li.append(chr(n))
        return print(*li, sep='')

    elif lang == 'ан':
        for i in range(len(s1)):
            if s1[i] in '.,?!"' or s1[i] == ' ':
                li.append(s1[i])
                continue
            if s1[i] == s1[i].upper():
                n = ord(s1[i]) - sdvig
                if n < 65:
                    n += 26
                li.append(chr(n))
            else:
                n = ord(s1[i]) - sdvig
                if n < 97:
                    n += 26
                li.append(chr(n))
        return print(*li, sep='')
    else:
        return print('我不懂這種語言')


if __name__ == '__main__':
    vib = input('Выберите : шифрование(ш) или дешифрование(д) ',)
    lan = input('Выберите на каком языке :  русский(ру) или английский(ан) ')
    sd = int(input('Выберите сдвиг: '))
    s = input('Какой текс используем ? ')

    if vib == 'ш':
        shifr(lan, sd, s)
        otv = 'да'
        while otv == 'да':
            otv = input('Желаете понять сдвиг? ')
            if otv == 'да':
                sd = int(input('Выберите сдвиг: '))
                shifr(lan, sd, s)
    elif vib == 'д':
        deshifr(lan, sd, s)
        otv = 'да'
        while otv == 'да':
            otv = input('Желаете понять сдвиг? ')
            if otv == 'да':
                sd = int(input('Выберите сдвиг: '))
                deshifr(lan, sd, s)

    else:
        print('Я вас не понимать')

    print('Приходи еще ...')
