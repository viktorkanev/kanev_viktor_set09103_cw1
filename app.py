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


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)