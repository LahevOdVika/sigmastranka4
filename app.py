from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html') # Render na base, hlavně na debug


if __name__ == '__main__':
    app.run(debug=True)