from random import *


def body(otv):
    global qua
    print('Спроси меня о чем-нибудь')
    qua = input()
    return print(choice(otv))


li = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай',
      'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
      'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
      'Определённо да', 'Знаки говорят - да',	'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
      'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как мне тебя называть?')
name = input()
print('Привет,', name)

qua = ''
a = 'Да'
while a == 'Да':
    body(li)
    print('Хочешь еще что-нибудь спросить', name, '?(Да/Нет)')
    a = input()
print('Возвращайся если возникнут вопросы!')
