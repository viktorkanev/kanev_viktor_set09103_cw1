from flask import Flask, render_template, json, jsonify, request, session, url_for, redirect
from artists import Artists
import bcrypt


app = Flask(__name__)

Artists = Artists()


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