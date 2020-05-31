age = abs(float(input('Введите свой возраст: ')))

def occupation(age):
    if age < 7:
        return 'детсадовец'
    elif 7 <= age < 18:
        return 'школьник'
    elif 18 <= age < 23:
        return 'студент'
    else:
        return 'работник'

person_occupation = occupation(age)
print (f'Вы {person_occupation}')

