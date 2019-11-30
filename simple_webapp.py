from flask import Flask, session

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/page1')
def page1() -> str:
    return 'This is page 1...fool!'

@app.route('/page2')
def page2() -> str:
    return 'This is...wait...Yeah, this is page 2.'

@app.route('/page3')
def page3() ->str:
    return '....Guess what...this is  page 3....yup.'

@app.route('/login')
def do_login() ->str:
    session['Logged_in']=True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('Logged_in')
    return 'You are now logged out.'

@app.route('/status')
def check_status() -> str:
    if 'Logged_in' in session:
        return 'You are still logged in.'
    return 'You are currently logged out.'

app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)

