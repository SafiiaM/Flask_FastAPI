from flask import Flask

app = Flask(__name__)
# @app.route('/')
#
# def index():
#     return 'Привет, незнакомец!'

@app.route('/Николай/')

def nike():
    return 'Привет, Николай!'
# Николай вставляем в браузер - http://127.0.0.1:5000/Николай
@app.route('/Иван/')

def ivan():
    return 'Привет, Иван!'

if __name__ == '__main__':
    app.run(debug=True)


