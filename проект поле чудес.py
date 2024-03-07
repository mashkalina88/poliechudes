#список слов, которые могут быть загаданы
words = ['собака', 'поле', 'игра', 'комната', 'картина', 'прилагательное', 'ваза', 'звезда', 'певец', 'магнитофон', 'тюльпан', 'цветы', 'наушники', 'наклейки', 'кондейционер']


#главынй цикл игры
while True:
    popitka = 0
    #выбор самого слова
    nomer_slova = int(input('Введи номер слова от 1 до 15'))
    secret = words[nomer_slova-1]
    user_let = [] #пустой список, в котором буду все буквы, которые вводит пользователь
    #цикл для ввода буквы и работы главной логики игры
    while True:
        popitka += 1
        plus = 0
        letter = input('\nбуква: ').lower()
        if len(letter) > 1 and len(letter) != len(secret) and '/' not in letter:
            print('Ты ввел больше, чем одну букву')
        elif '/help' in letter:
            print('rulls')
        else:
            if letter in user_let:
                print('Такая буква уже есть')
            else:
                user_let.append(letter)
                for i in secret:
                    if i in user_let:
                        print(i, end = ' ')
                    else:
                        print('_', end = ' ')
                        plus += 1
                if plus == 0:
                    print('\nТы победил')
                    print('\nКоличество попыток: ', popitka)
                    break
