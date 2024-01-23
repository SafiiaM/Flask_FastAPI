from flask import Flask
from flask_wtf.csrf import CSRFProtect

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

@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'

if __name__ == '__main__':
    app.run(debug=True)