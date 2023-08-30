name = input('Как вас зовут?')
questions = [
    {'question': 'Когда Маринетт влюбилась в Адриана?',
     'answers': ['Летом, увидев его на странице журнала', 'В первый день учёбы, встретив его в классе',
                 'В момент, когда он подал ей зонтик'],
     'right_answer': 3},
    {'question': 'Кто первый узнал личность Леди баг?',
     'answers': ['Аля Сезер', 'Лука Куффен', 'Адриан Агрест'],
     'right_answer': 1},
    {'question': 'Зачем Бражнику(Монарху) камни чудес?',
     'answers': ['Захватить мир', 'Вернуть к жизни свою жену', 'Он просто вредный'],
     'right_answer': 2},
    {'question': 'Как зовут квами-пчелу?',
     'answers': ['Поллен', 'Триккс', 'Нууру'],
     'right_answer': 1},
    {'question': 'Как зовут Луку Куффена в облике супергероя?',
     'answers': ['Карапас', 'Минотавр', 'Вайперион'],
     'right_answer': 3}
]
points = 0
for question in questions:
    print(question.get('question'))
    counter_answer = 0
    for answer in question.get('answers'):
        counter_answer += 1
        print(counter_answer, ')', answer)
    user_answer = int(input('Выберите верный вариант ответа: '))
    if user_answer == question.get('right_answer'):
        print('Верно!')
        points += 1
    else:
        print('Ответ неверный :(')
    print('_' * 100)
print('Ваш счёт правильных ответов:', points)
if points >= 3:
    print('Ты победил!')
else:
    print('Ты проиграл :(')

f = open('results.txt', 'a', encoding='utf-8')
f.write("Игрок" + name + " набрал " + str(points) + ' очков.\n')