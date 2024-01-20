import secrets

from flask import Flask, render_template, request, redirect, url_for, flash, session
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
# app.secret_key = b'c423f4b59a70b582423d155cea9ca9be21631494c5d24fb0331985201466d3f5'
app.secret_key = secrets.token_hex()

category = [
    {"title": 'Home page', "func_name": 'index'},
    {"title": 'Button page', "func_name": 'button'},
    {"title": 'Image page', "func_name": 'image'},
    {"title": 'Upload image page', "func_name": 'image_get'},
    {"title": 'Login page', "func_name": 'login'},
    {"title": 'Send text page', "func_name": 'send'},
    {"title": 'Calculate page', "func_name": 'calc'},
    {"title": 'Check age page', "func_name": 'check_age'},
    {"title": 'Square page', "func_name": 'square'},
    {"title": 'Flash page', "func_name": 'flas'},
    {"title": 'Log page', "func_name": 'log'}
]

users = ['John', 'Olga', 'Smith','Safiia']
info = {
    'John': '123',
    'Olga': 'qwerty',
    'Smith': '12345',
    'Safiia': '1969'
}


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)

"""
1. Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.
"""
@app.route('/button/', methods=['GET', 'POST'])
def button():
    if request.method == 'POST':
        return 'Hello Bob'
    return render_template('button.html')

"""
2. Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма для загрузки изображений.
"""
@app.route('/image/')
def image():
    return render_template('image.html')


@app.get('/upload/')
def image_get():
    return render_template('upload.html')


@app.post('/upload/')
def image_post():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
    return f"Файл {file_name} загружен на сервер"

"""
3. Создать страницу, на которой будет форма для ввода логина и пароля

При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.
"""
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and password == info[username]:
            return   'Welcome Home, Your Majesty!'
        else:
            return f'Hello, {username}'
    return render_template('login.html')
    # return redirect (url_for('index'))

"""
4.
Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить".

При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
"""
@app.route('/send_text/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        text = escape(request.form.get('text'))
        return f"количество слов {len(text.split(' '))}"
    return render_template("text.html")

"""
5. Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить"

При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.
"""
@app.route('/calculate/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        first = float(request.form.get('firstnum'))
        second = float(request.form.get('secondnum'))
        operation = request.form.get('operation')
        res = 0
        match operation:
            case "+":
                res = first + second
            case "-":
                res = first - second
            case "/":
                res = first / second
            case "*":
                res = first * second
        return f"{first} {operation} {second} = {res}"
    return render_template('calculate.html')

"""
6. Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"

При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.
"""
@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        age = int(request.form.get('age'))
        if age >= 18:
            return "Можно"
        return "Нельзя"
    return render_template('check_age.html')
"""
7. Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"

При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число и его квадрат.
"""
@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('square.html')

"""
8. Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"

При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет выведено "Привет, {имя}!".
"""
@app.route('/flas/', methods=['GET', 'POST'])
def flas():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flas'))
    return render_template('flas.html')

"""
9. Создать страницу, на которой будет форма для ввода имени и электронной почты При отправке которой будет создан cookie файл с данными пользователя

Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка "Выйти" При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""
@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)