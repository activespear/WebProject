from flask import Flask, url_for, render_template
import sqlite3
from geocode_root import show_on_map

app = Flask(__name__)
con = sqlite3.connect('DostSeeker.db')
cur = con.cursor()
result = cur.execute("""SELECT form FROM Forms""").fetchall()
for i in range(len(result)):
    result[i] = result[i][0]
result1 = cur.execute("""SELECT subject FROM subjects""").fetchall()
for i in range(len(result1)):
    result1[i] = result1[i][0]


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['cssloc'] = url_for('static', filename='css/style.css')
    image = 'Photo.png'
    classes = result
    subjects = result1
    return render_template('main.html', **param, sub_list=subjects, classes_list=classes, img=image)


@app.route('/mail')
def mail():
    return index()


@app.route('/login')
def login():
    return render_template('login.html', )


if __name__ == '__main__':    app.run(port=8080, host='127.0.0.1')
