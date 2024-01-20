# Flash сообщения

from flask import Flask, flash, redirect, render_template,request, url_for

app = Flask(__name__)

app.secret_key = b'c423f4b59a70b582423d155cea9ca9be21631494c5d24fb0331985201466d3f5'

""" 
Генерация надежного секретного ключа
>>> import secrets # открываем Python Console и вводим эту строку
>>> secrets.token_hex() # затем вводим эту строку , получаем ключ 
'c423f4b59a70b582423d155cea9ca9be21631494c5d24fb0331985201466d3f5'
"""
@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')

if __name__ == '__main__':
    app.run(debug=True)