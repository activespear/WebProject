from flask import Flask, url_for
import requests
import json
from geocode_root import show_on_map

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>&nbsp;-&nbsp;DostSeeker.com&nbsp;-&nbsp;</title>
                      </head>
                      <body>
                            <table class="mainTable">
                                <tr>
                                    <td class="mainTableTd">
                                        <table width="100%">
                                            <tr>
                                                <td class="headerTableTd" width="150px" align="center"><a href="/">Главная</a></td>
                                                <td class="headerTableTd" width="*" align="center">&nbsp;<b>DostSeeker.com</b>&nbsp;</td>
                                                <td class="headerTableTd" width="15px"><a href="/mail">&#X2709;</a></td>
                                                <td class="headerTableTd" width="150px" align="center"><a href="/login">Авторизоваться</a></td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="mainTableTd">
                                        <table width="100%">
                                            <tr style="vertical-align: top;">
                                                <td class="contentTableTd" width="220px">
                                                    <table>
                                                        <tr><td align="center"><b>Фильтр</b></td></tr>
                                                        <tr><td>{_get_class_filter()}</td></tr>
                                                        <tr><td>{_get_subject_filter()}</td></tr>
                                                    </table>
                                                </td>
                                                <td class="contentTableTd" width="*" height="500px" align="center"><b>Карта</b></td>
                                                <td class="contentTableTd" width="265px" align="center"><b>Описание</b></td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                      </body>
                    </html>"""

@app.route('/mail')
def mail():
    return index()

@app.route('/login')
def login():
    return index()

def _get_class_filter():
    return f"""<select name="class" style="width: 150px;">
        <option value="">Выберите класс</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
        <option value="11">11</option>
    </select>"""


def _get_subject_filter():
    return f"""<select name="subject" style="width: 150px;">
        <option value="">Выберите предмет</option>
        <option value="История">История</option>
        <option value="География">География</option>
        <option value="Биология">Биология</option>
    </select>"""

@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''

# @app.route('/image_sample')
# def image():
#     return '''<img src="{}" alt="здесь должна была быть картинка, но не нашлась">'''.format(url_for('static', filename='img/webserver-1-7.jpeg'))




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


# @app.route('/form_sample', methods=['POST', 'GET'])
# def form_sample():
#     if request.method == 'GET':
#         return f'''<!doctype html>
#                         <html lang="en">
#                           <head>
#                             <meta charset="utf-8">
#                             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                             <link rel="stylesheet"
#                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
#                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
#                             crossorigin="anonymous">
#                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
#                             <title>Пример формы</title>
#                           </head>
#                           <body>
#                             <h1>Форма для регистрации в суперсекретной системе</h1>
#                             <div>
#                                 <form class="login_form" method="post">
#                                     <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
#                                     <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
#                                     <div class="form-group">
#                                         <label for="classSelect">В каком вы классе</label>
#                                         <select class="form-control" id="classSelect" name="class">
#                                           <option>7</option>
#                                           <option>8</option>
#                                           <option>9</option>
#                                           <option>10</option>
#                                           <option>11</option>
#                                         </select>
#                                      </div>
#                                     <div class="form-group">
#                                         <label for="about">Немного о себе</label>
#                                         <textarea class="form-control" id="about" rows="3" name="about"></textarea>
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="photo">Приложите фотографию</label>
#                                         <input type="file" class="form-control-file" id="photo" name="file">
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="form-check">Укажите пол</label>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
#                                           <label class="form-check-label" for="male">
#                                             Мужской
#                                           </label>
#                                         </div>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="female" value="female">
#                                           <label class="form-check-label" for="female">
#                                             Женский
#                                           </label>
#                                         </div>
#                                     </div>
#                                     <div class="form-group form-check">
#                                         <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
#                                         <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
#                                     </div>
#                                     <button type="submit" class="btn btn-primary">Записаться</button>
#                                 </form>
#                             </div>
#                           </body>
#                         </html>'''
#     elif request.method == 'POST':
#         print(request.form['email'])
#         print(request.form['password'])
#         print(request.form['class'])
#         print(request.form['file'])
#         print(request.form['about'])
#         print(request.form['accept'])
#         print(request.form['sex'])
#         return "Форма отправлена"