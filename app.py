from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return render_template("nav.html","index.html")

@app.route('/members')
def members():  # put application's code here
    return render_template("members.html")

@app.route('/nav')
def nav():  # put application's code here
    return render_template("nav.html")
if __name__ == '__main__':
    app.run()
