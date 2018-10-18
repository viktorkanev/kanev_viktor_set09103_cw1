from flask import Flask, render_template, json, request, session, url_for, redirect, flash
from artists import Artists
from users import Users
from functools import wraps


app = Flask(__name__)
app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX/,?RT'
Artists = Artists()

def check_auth(email, password):
   user_data = json.load(open('users.json'))
   if(email == user_data.get('email') and  password == user_data.get('password')):
        return True
   return False

def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        status = session.get('logged_in', False)
        if not status:
            flash(u'You have to be logged in to access this page.', 'error')
            return redirect(url_for('.login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['email']
        pw = request.form['password']

        if check_auth(request.form['email'],request.form['password']):
            session['logged_in']= True
            return redirect(url_for('.dashboard'))
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/collections')
def collections():
   return render_template('collections.html', artists=Artists)


@app.route('/collections/<string:name>/')
def artist(name):
    return render_template('artists.html', name=name, artists=Artists)

@app.route('/genrecol/<string:genre>/')
def genre(genre):
    return render_template('genre.html', genre=genre, artists=Artists)

@app.route('/genrecol')
def genrecol():
    return render_template('genrecol.html', artists=Artists)

@app.route('/dashboard', methods = ['POST', 'GET'])
@requires_login
def dashboard():
    if request.method == 'POST':
        name = request.form['name']
        Artists.update({'name':name})
    return render_template('dashboard.html')


# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     form = request.form
#     if request.method == 'POST':
#         email = form.get('email')
#         password = form.get('passoword')
#         return "your email is:" + email



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)