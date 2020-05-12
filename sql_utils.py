import sqlite3


def get_classes():
    con = sqlite3.connect('DostSeeker.db')
    cur = con.cursor()
    result = cur.execute("""SELECT form FROM Forms""").fetchall()
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def get_subjects():
    con = sqlite3.connect('DostSeeker.db')
    cur = con.cursor()
    result = cur.execute("""SELECT subject FROM subjects""").fetchall()
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def get_places(form, subj):
    if form == "" or subj == "":
        return ""
    con = sqlite3.connect('DostSeeker.db')
    cur = con.cursor()
    result = cur.execute(f"""SELECT Place FROM Lessons 
                    WHERE Form= '{form}' AND Subject = '{subj}'""").fetchall()
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def get_lesson(form, subj, place):
    con = sqlite3.connect('DostSeeker.db')
    cur = con.cursor()
    result = cur.execute(f"""SELECT Lesson FROM Lessons
                    WHERE Form = '{form}' AND Subject = '{subj}' AND Place = '{place}'""").fetchall()[0]
    return result


def do_login(loginIN, passwordIN):
    con = sqlite3.connect('DostSeeker.db')
    cur = con.cursor()
    message = ''
    login = cur.execute(f"""SELECT login FROM Users
                    WHERE login = '{loginIN}'""").fetchall()
    if not len(login):
        message = 'Такого пользователя нет'
    else:
        password = cur.execute(f"""SELECT password FROM Users
                    WHERE login = '{loginIN}'""").fetchall()[0][0]
        print(password)
        print(passwordIN)
        if password != passwordIN:
            message = 'Пароль неверный'
    return message

