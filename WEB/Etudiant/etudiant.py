import flask
import psycopg2

#!!
#tests webs
#!!

app = flask.Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('acceuil.html', name=name)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('acceuil.html', name=name)

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        log()
    else:
        show_the_login_form()

def log():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)

if __name__ == '__main__':

    app.run()
