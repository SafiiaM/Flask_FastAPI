from flask import Flask, render_template
from models_05 import  db, User

app = Flask(__name__, instance_path='/Flask_FastAPI/seminar_2/app_05-instance/mydatabase.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../var/instance/mydatabase.db'
db.init_app(app)




@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)

if __name__ == '__main__':
    app.run(debug=True)