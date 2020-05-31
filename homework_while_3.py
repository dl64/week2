mydict = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", 'Как погода?': 'Солнечно!'}

while True:
    user_question = input('Спроси меня вопрос: ')
    print(mydict.get(user_question, 'не знаю, что ответить'))
