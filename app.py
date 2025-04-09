from flask import Flask, render_template, request
from dbHandler import databaseHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home/index.html')

@app.route('/base')
def base():
    return render_template('base.html') # Render na base, hlavně na debug

@app.route('/kontakt', methods=['POST', 'GET'])
def kontakt():
    if request.method == 'POST':
        with databaseHandler() as db:
            db.addUser(request.form['name'], request.form['email'], request.form['phoneNumber'], request.form['message'])
    return render_template('kontakt/kontakt.html')

@app.route('/iphone')
def iphone():
    with databaseHandler() as db:
        return render_template('order/order.html', phone_models=db.getPhoneModels())

if __name__ == '__main__':
    app.run(debug=True)