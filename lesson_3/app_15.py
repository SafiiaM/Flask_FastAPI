from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'ee8d3ba248c4fe119ec1a8c777e5fe1b53473608a65753999c3b301034881663'
# 'mysecretkey' = 'ee8d3ba248c4fe119ec1a8c777e5fe1b53473608a65753999c3b301034881663'
csrf = CSRFProtect(app)

"""
Генерация надежного секретного ключа 
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)