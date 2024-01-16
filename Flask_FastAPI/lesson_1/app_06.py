# Рендеринг HTML файла

from flask import Flask
from flask import render_template # импортируем функцию отрисовки шаблонов. render_template()
# принимает в качестве первого аргумента название html-файла, который необходимо вывести в браузер.

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'
@app.route('/index/')
def html_index(): # Добавим функцию рендеринга в функцию представления и укажем ей на файл index.html.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)