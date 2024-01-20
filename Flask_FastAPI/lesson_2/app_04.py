from flask import Flask, request #Обработка GET запросов
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hi!'

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'
#  http://127.0.0.1:5000/get/?name=alex&age=13&level=80

if __name__ == '__main__':
    app.run(debug=True)