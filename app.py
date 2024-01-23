from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Mock user data (replace this with your actual user data)
users = [
    {'username': 'MaxxieMax', 'password': 'root'},
    {'username': 'user2', 'password': 'pass2'},
]

def authenticate_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            return redirect(url_for('dashboard', username=username))

    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
