from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'birthday_secret_key_for_buba'

# كلمة السر المطلوبة
PASSWORD = "بوبا"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_password = request.form.get('password')
        if user_password == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('birthday'))
        else:
            error = "كلمة السر خاطئة يا قمر! جربي تاني 🩷"
    return render_template('login.html', error=error)

@app.route('/birthday')
def birthday():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)