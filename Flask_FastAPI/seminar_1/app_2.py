"""
2. Дорабатываем задачу 1. Добавьте две дополнительные страницы в ваше вебприложение:

страницу "about"
страницу "contact".

3. Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

4. Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

5. Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".

"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'

@app.route('/sum/<int:a>/<int:b>/')
def sum_num(a, b):
    return f'{a}+{b}={a + b}'

@app.route('/string/<string:text>/')
def string(text):
    return str(len(text))
@app.route('/index/')
def index():
    return render_template('base.html')
if __name__ == "__main__":
    app.run(debug=True)