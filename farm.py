import keyboard
try:
    print('Приветствую в программе Галимова!')
    dictionary = { "яблоко": {"apple", "pome"}, "банан": {"banana"}, "груша": {"pear"}, "апельсин": {"orange"}, "киви": {"kiwi"} }
    possible_keys = ['ctrl+f', 'esc', 'tab','shift']
    print('**Памятка**')
    print('нажмите "ctrl+f"  для поиска слова в словаре')
    print('нажмите "+" для добавления в словарь ')
    print('нажмите "tab"  для дополнительного перевода')
    print('нажмите "enter" для завершения ввода слова')
    print('нажмите "esc" для завершения задачи')
    print('**Памятка**')
    while True:
        if keyboard.is_pressed('ctrl+f'):
            info=input('Введите слово для проверки в списке: ')
            if info in dictionary:
                print(dictionary[info])
            else:
                print('Такого слова нет!')
            break

        if keyboard.is_pressed('esc'):
            print('Работа завершена! До свидания!')
            break
        if keyboard.is_pressed('+'):
            translation= set()
            input_original=input('Введите слово на Русском языке: ')
            input_translation=input("Введите перевод слова(на Английском) ")
            if input_original in dictionary or input_translation in dictionary:
                print('Такое слово уже есть,ведите другое название')
                break
            dictionary[input_original] = input_translation
            translation.add(input_original)
            translation.add(input_translation)
            print(f'Слово {input_original} и перевод {dictionary[input_original]} добавлены в словарь')
            print('Чтобы добавить дополнительный перевод нажмите "tab"')

        while True:
            if keyboard.is_pressed('tab'):
                    add_translation = input('Введите дополнительный перевод: ')
                    dictionary[input_original] = input_translation, add_translation.replace("\t","")
                    print(f'Весь список: {dictionary}')
            if keyboard.is_pressed('shift'):
                break
except ValueError as e:
    print("Некорректный ввод данных!")