from flask import Flask, render_template, json, request, session, url_for, redirect, flash
from artists import Artists
from users import Users
import bcrypt
from functools import wraps


app = Flask(__name__)
app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX/,?RT'
Artists = Artists()
Users = Users()

def check_auth(email, password):
   for user in Users:
        useremail = user.get('email')
        userpw = user.get('password')
        print(userpw)
   if(email == useremail and  password == userpw):
        return True
   return False

def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        status = session.get('logged_in', False)
        if not status:
            return redirect(url_for('.root'))
        return f(*args, **kwargs)
    return decorated

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('.root'))

@app.route('/login', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        user = request.form['email']
        pw = request.form['password']

        if check_auth(request.form['email'],request.form['password']):
            session['logged_in']= True
            flash('You were successfully logged in!')
            return redirect(url_for('.collections'))
    return render_template('login.html')

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