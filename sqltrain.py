#Это для выбора места после того, как оно будет выбрано в фильтрах: выбирают класс предмет, выдают: form, subj,
#Потом на основе выбранных в первой фазе токенов и выбранного в второй фазе токена нажать на кнопку, перед этим:
#выбрать 3е
result2 = cur.execute(f"""SELECT Place FROM Lessons 
                WHERE Form= '{form}' AND Subject = '{subj}'""").fetchall()
for i in range(len(result2)):
    result2[i] = result2[i][0]
#для выбора третьего
name = cur.execute(f"""SELECT Lesson FROM Lessons
                WHERE Form = '{form}' AND Subject = '{subj}' AND Place = '{place}'""").fetchall()[0]
#теперь метаданные для выбранного места
image = f'static/meta/img/{name}.png'
text = open(f'static/meta/text/{name}.txt', 'r')
text = text.read().split('\n')
#замена изначальной карты кастомной
show_on_map(name)
#логин и пароль
loginIN = ''
passwordIN = ''
login = cur.execute(f"""SELECT login FROM Users
                WHERE login = '{loginIN}'""").fetchall()[0]
if login == 'NULL':
    message = 'Такого пользователя нет'
else:
    password = cur.execute(f"""SELECT password FROM Users
                WHERE login = '{loginIN}'""").fetchall()[0]
    if password == passwordIN:
        message = 'ok'
    else:
        message = 'Пароль неверный'
