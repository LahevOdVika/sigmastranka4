from flask import Flask, render_template, request
from dbHandler import databaseHandler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home/index.html')

@app.route('/base')
def base():
    return render_template('base.html') # Render na base, hlavně na debug

@app.route('/kontakt', methods=['POST', 'GET'])
def kontakt():
    if request.method == 'POST':
        with databaseHandler() as db:
            db.addUser(request.form['name'], request.form['email'], request.form['phoneNumber'],
                       request.form['message'])
    return render_template('kontakt/kontakt.html')


@app.route('/iphone', methods=['POST', 'GET'])
def iphone():
    with databaseHandler() as db:
        return render_template('order/order.html', phone_models=db.getPhoneModels())

@app.route('/design', methods=['POST', 'GET'])
def design():
    if request.method == 'POST':
        model = request.form.get('model')
        if not model:
            return 'Model nebyl poskytnut.', 400
        with databaseHandler() as db:
            if db.checkPhoneExistence(model):
                print(model)
                return render_template('design/design.html', model=model)
            else:
                return 'Žádný obal pro tento model.', 400
            
@app.route('/galerie')
def galerie():
    return 'Galerie guh'


if __name__ == '__main__':
    app.run(debug=True)