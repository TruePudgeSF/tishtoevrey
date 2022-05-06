import time
xal=1
if xal==1:
    for a in '9:07 Кабинет 28 6И урок русского. Ольга Михайловна опять опоздала на первый урок.Училка разговаривает с учениками по поводу самостоятельной работы, которую они писали ранее':
        print(a, end='')
    print('.\n')
    time.sleep(0.6)
    for a in 'Ольга Михайловна: Надеюсь вы ознакомились с результатами работы. КАК МОЖНО БЫЛО НАПИСАТЬ ЕЕ ТАК ПЛОХО? ПОЧТИ НИ ОДНОЙ ПЯТЕРКИ ЗА КЛАСС!!':
        print(a, end='')
    print('\n')
    for a in 'Ты: *Ну за эту работу я не ожидал получить хорошую оценку*':
        print(a, end='')
    print('.\n')
    time.sleep(0.6)
    for a in '*Получаешь работу*':
        print(a, end='')
    print('.\n')
    time.sleep(0.8)
    for a in 'Ты: Фух, вроде пронесло.':
        print(a, end='')
    time.sleep(0.7)
    for a in '4':
        print(a,end='')
    time.sleep(0.7)
    print('\n')
    for a in '*Боря получает работу*':
        print(a, end='')
    print('.\n')
    time.sleep(0.6)
    for a in 'Ты: Слушай, а какая у тебя оценка?':
        print(a,end='')
    print('\n')
    time.sleep(0.7)
    for a in 'Боря: Погоди щас посмотрю...':
        print(a,end='')
    print('\n')
    time.sleep(0.9)
    for a in 'Боря: ЕБУШКИ ВОРОБУШКИ. 3-':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ты: Погоди это хорошо или плохо? ':
        print(a,end='')
    time.sleep(0.7)
    for a in 'Хотя учитывая твои оценки это...':
        print(a,end='')
    print('\n')
    time.sleep(0.7)
    for a in 'Боря: Это заебенно! Мы с мамой в честь этого барашка заколем!':
        print(a,end='')
    print('\n')
    time.sleep(0.7)
    for a in 'Ты: Погоди...Ты что еврей?':
        print(a,end='')
    time.sleep(1)
    for a in ' Хотя ладно не суть...':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in '*Ерофей подходит к тебе*':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ерофей: Привет, какая у тебя оценка?':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ты: 4, а у тебя?':
        print(a,end='')
    print('\n')
    time.sleep(0.6)
    for a in 'Ерофей: 5- за полторы ошибки)':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ты: Погоди-ка... У меня тоже полторы ошибки! И 4!!!!':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ты: Ольга Михайловна!':
        print(a,end='')
    print('\n')
    time.sleep(0.8)
    for a in 'Ольга Михайловна:Аааа? Ч-Что?':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ты: Почему у меня за полторы ошибки 4, а у Ерофея 5-?':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Ольга михайлонва:а-а... Знаешь, я точно видела что ты дал списывать Боре, поэтому у меня были полные основания поставить тебе 4':
        print(a,end='')
    print('\n')
    time.sleep(0.8)
    for a in 'Боря: ЧТООО?':
        print(a,end='')
    print('\n')
    time.sleep(0.7)
    for a in 'Ты: ЧТООО?':
        print(a,end='')
    print('\n')
    time.sleep(1)
    for a in 'Выбрать док-во: Мой тест, тест Бори(1 или 2)':
        print(a,end='')
    print('\n')
    b=int(input())
    if b==1:
        for a in 'Ты: Посмотрите на мой тест! Я никак не мог дать списать Боре!':
            print(a,end='')
        print('\n')
        time.sleep(1)
        for a in 'Ольга михайловна: Ты ничего не доказал! Ты проиграл!':
            print(a,end='')
        print('\n')
    elif b==2:
        for a in 'Ты: Посмотрите на тест Бори!':
            print(a,end='')
        print('\n')
        time.sleep(0.7)
        for a in 'Тест Бори добавлен в материалы дела':
            print(a,end='')
        print('\n')
        time.sleep(0.9)
        for a in 'Ты: Там, где у меня ошибки, у Бори наоборот правильные ответы, а в остальном у него все неправльно!':
            print(a,end='')
        print('\n')
        time.sleep(1)
        for a in 'Ольга Михайловна: Аа? Х-хотя знаешь, у тебя один из терминов написаан  некорректно и я посставила тебе 4':
            print(a,end='')
        print('\n')
        time.sleep(1)
        for a in 'Выбрать док-во: Мой тест, сравнение с тестом ерофея':
            print(a,end='')
        print('\n')
        b=int(input())
        if b==2:
            for a in 'Ты: У нас с Ерофеем все термины полностью совпадают':
                print(a,end='')
            print('\n')
            time.sleep(1)
        elif b==1:
            for a in 'Ты :Посмотрите на обратную сторону моего листка':
                print(a,end='')
            print('\n')
            time.sleep(1)
            for a in 'Ты: Я выделил выделителем те термины, которые я написал. Их всего три как и должно быть':
                print(a,end='')
            print('\n')
            time.sleep(1.3)
            for a in 'И ПОД ВСЕМИ ПОСТАВЛЕНЫ ПЛЮСЫ!':
                print(a,end='')
            print('\n')
            time.sleep(1.2)
            for a in 'Ольга Михайловна:':
                print(a,end='')
            print('\n')   
            time.sleep(1)
