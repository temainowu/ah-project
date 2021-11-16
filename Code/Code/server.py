from flask import Flask, render_template, request
from passwords import hash_password, check_password
from User import User, add_user

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/", methods = ['GET'])
def do():
    move = request.form['move']
    return move

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/login/passwordreset")
def passwordreset():
    return render_template('passwordreset.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signup", methods = ['POST'])
def newAccount():
    name = request.form['username']
    score = 0
    question = request.form['question']
    answer_hash = hash_password(request.form['answer'])
    password_hash = hash_password(request.form['password'])
    add_user(name, score, question, answer_hash, password_hash)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
    
