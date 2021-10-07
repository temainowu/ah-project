from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/math")
def math():
    return render_template('math.html')


@app.route("/code")
def code():
    return render_template('code.html')


@app.route("/lang")
def lang():
    return render_template('lang.html')


if __name__ == '__main__':
    app.run(debug=True)
