#список слов, которые могут быть загаданы
words = ['собака', 'поле', 'игра', 'комната', 'картина', 'прилагательное', 'ваза', 'звезда', 'певец', 'магнитофон', 'тюльпан', 'цветы', 'наушники', 'наклейки', 'кондейционер']
alfabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ш', 'щ', 'ч', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

#главынй цикл игры
while True:
    popitka = 0
    #выбор самого слова
    print('Список команд:\n/help - правила игры')
    nomer_slova = int(input('Введи номер слова от 1 до 15\n'))
    secret = words[nomer_slova-1]
    user_let = [] #пустой список, в котором буду все буквы, которые вводит пользователь
    #цикл для вывода символов вместо букв в загаданном слове
    for i in secret:
        print('_', end = ' ')
    #цикл для ввода буквы и работы главной логики игры
    while True:
        popitka += 1
        plus = 0
        letter = input('\nбуква: ').lower()
        if (len(letter) > 1) and ('/' not in letter) or (letter not in alfabet):
            if len(secret) == len(letter):
                if secret == letter:
                    print('Ты победил')
                    break
                else:
                    print('попробуй еще раз')
            else:
                print('ты ввел больше, чем одну буву или не букву')
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
