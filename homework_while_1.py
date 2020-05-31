while True:
    user_answer1 = input('Как дела? ')
    if user_answer1 == 'Хорошо':
        print('Молодец! Вопросов больше нет!')
        print('*****')
        break
    else:
        print('Разве "{}" это подходящий ответ?'.format(user_answer1))
        print('Попробуй еще разок. Как дела?')
        print('=====')

