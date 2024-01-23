from flask import Flask
from Flask_FastAPI.lesson_3.models_05 import  db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hi!'

@app.cli.command("init-db") #Создание таблиц в базе данных
def init_db():
    db.create_all()
    print('OK')

if __name__ == '__main__':
    app.run(debug=True)