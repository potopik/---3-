alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
vibor = str(input('Если вы хотите провести шифровку введите y, если дешифровку n '))
itog = ''
if vibor == 'Y' or vibor == 'y':
    shag = int(input('Введите шаг сдвига от 1 до 33'))
    if shag <= 0 or shag > 33:
        print('Некорректный шаг')
    else:
        phrase = str(input('Введите высказывание  для шифрования'))
        for i in phrase:
            position = alfabet.find(i)
            position2 = position + shag
            if i in alfabet:
                itog = itog + alfabet[position2]
            else:
                itog = itog + i
        print('Зашифрованное сообщение', itog)
elif vibor == 'N' or vibor == 'n':
    shag = int(input('Введите шаг сдвига от 1 до 33'))
    if shag <= 0 or shag > 33:
        print('Некорректный шаг')
    else:
        phrase = str(input('Введите высказывание  для дешифрования'))
        for i in phrase:
            position = alfabet.find(i)
            position2 = position - shag
            if i in alfabet:
                itog = itog + alfabet[position2]
            else:
                itog = itog + i
        print('Расшифрованное сообщение', itog)
else:
    print('Некорректная команда')
