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
                        <!--h1>Первая HTML-страница</h1-->
                            <table class="mainTable">
                                <tr>
                                    <td class="mainTableTd">
                                        <table>
                                            <tr>
                                                <td class="headerTableTd">Главная</td>
                                                <td class="headerTableTd" width="100%" align="center">&nbsp;<b>DostSeeker.com</b>&nbsp;</td>
                                                <td class="headerTableTd">&#X2709;</td>
                                                <td class="headerTableTd">Log&nbsp;in</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="mainTableTd">
                                        <table>
                                            <tr style="vertical-align: top;">
                                                <td class="contentTableTd" align="center">Фильтр</td>
                                                <td class="contentTableTd" width="100%" height="500px" align="center">Карта</td>
                                                <td class="contentTableTd" align="center">Описание</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                      </body>
                    </html>"""

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