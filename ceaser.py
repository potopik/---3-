def is_digit(num_str): # функция на проверку корректности шага(введения только цифр)
    return num_str.replace('.', '', 1).lstrip('-').isdigit()


alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя' # Задаем переменную с двойным алфавитом для шифрования последних букв
vibor = str(input('Если вы хотите провести шифровку введите y, если дешифровку n ')) # Задаем переменную для выбора расшифровки или шифровки
itog = ''
if vibor == 'Y' or vibor == 'y': #Блок предназначенный для шифровки
    shag = input('Введите шаг сдвига от 1 до 33')
    shag = is_digit(shag)
    if (shag > 0) and (shag <= 33):
        phrase = str(input('Введите высказывание  для шифрования'))
        phrase = phrase.lower() # Превращение верхнего регистра в нижний
        for i in phrase: # Цикл for, чтобы обратится к каждой букве по её номеру
            position = alfabet.find(i) # Обращается к элементам alfabet, для поиска совпадений
            position2 = position + shag # К индексу буквы добавляем шаг
            if i in alfabet:
                itog = itog + alfabet[position2]  # Внесение буквы в новую строку
            else:
                itog = itog + i # Внесение символа из не русского алфавита
        print('Зашифрованное сообщение', itog)
    else:
        print('Некорректный шаг')
elif vibor == 'N' or vibor == 'n':# Блок предназначенный для расшифровки
    shag = input('Введите шаг сдвига от 1 до 33')
    shag = is_digit(shag)
    if (shag > 0) and (shag <= 33):
        phrase = str(input('Введите высказывание  для дешифрования'))
        phrase = phrase.lower()
        for i in phrase:
            position = alfabet.find(i)
            position2 = position - shag # Еинственное отличие от предыдущего блока: от индекса буквы отнимаем шаг
            if i in alfabet:
                itog = itog + alfabet[position2]
            else:
                itog = itog + i
        print('Расшифрованное сообщение', itog)
    else:
        print('Некорректный шаг')
else:
    print('Некорректная команда')
