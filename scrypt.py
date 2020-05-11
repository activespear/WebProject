from flask import Flask, url_for, render_template
from data import db_session
import geocode_root

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['cssloc'] = url_for('static', filename='css/style.css')
    classes = [8, 9, 10]
    subjects = ['asd', 'asd']
    return render_template('main.html', **param, sub_list=subjects, classes_list=classes)


@app.route('/mail')
def mail():
    return index()


@app.route('/login')
def login():
    return render_template('login.html', )


# @app.route('/image_sample')
# def image():
#     return '''<img src="{}" alt="здесь должна была быть картинка, но не нашлась">'''.
#     format(url_for('static', filename='img/webserver-1-7.jpeg'))


if __name__ == '__main__':
    db_session.global_init("db/blogs.sqlite")
    app.run(port=8080, host='127.0.0.1')
