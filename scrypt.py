from flask import Flask, url_for, render_template, request, redirect
import sql_utils as sql
from geocode_root import show_on_map

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    class_value = ""
    subject_value = ""
    place_value = ""
    if request.method == 'POST':
        class_value = request.form.get('class')
        subject_value = request.form.get('subject')
        place_value = request.form.get('place')

    param = {}
    param['cssloc'] = url_for('static', filename='css/style.css')
    param['img'] = 'static/img/map.png'
    param['text'] = "Здесь будет текст"
    param['sub_list'] = sql.get_subjects()
    param['classes_list'] = sql.get_classes()
    param['places_list'] = sql.get_places(class_value, subject_value)

    if class_value and subject_value and place_value:
        lesson = sql.get_lesson(class_value, subject_value, place_value)
        param['img'] = f'static/meta/img/{lesson}.png'
        text = open(f'static/meta/text/{lesson}.txt', 'r')
        text = text.read().split('\n')
        param['text'] = '<br />'.join(text)

    return render_template('main.html', **param,
                           class_value=class_value, subject_value=subject_value, place_value=place_value)


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        login_value = request.form.get('login')
        password_value = request.form.get('password')
        message = sql.do_login(login_value, password_value)
        if message == '':
            return redirect('/')

    param = {}
    param['cssloc'] = url_for('static', filename='css/style.css')
    param['message'] = message
    return render_template('login.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
