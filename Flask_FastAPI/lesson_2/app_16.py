from flask import Flask, request, make_response, render_template, session, redirect, url_for # Сессии

app = Flask(__name__)

app.secret_key = b'c423f4b59a70b582423d155cea9ca9be21631494c5d24fb0331985201466d3f5'

@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')

@app.route('/logout/')
def logout():
        session.pop('username', None)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)