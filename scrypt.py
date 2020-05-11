from flask import Flask, url_for, render_template
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


if __name__ == '__main__':    app.run(port=8080, host='127.0.0.1')
