from flask import Flask, url_for, render_template #Генерация пути к статике
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hi!'

@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Харитон',
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
