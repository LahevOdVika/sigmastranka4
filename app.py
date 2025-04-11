import datetime
import os.path
from traceback import print_tb

from flask import Flask, render_template, request, url_for
from dbHandler import databaseHandler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

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
        return render_template('design/design.html', model=model)

@app.route('/refresh-editor', methods=['POST', 'GET'])
def refreshEditor():
    if request.method == 'POST':
        try:
            img = request.files['img']
            if img.filename != '':
                current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], current_time + os.path.splitext(img.filename)[1])
                img.save(filepath)
                return render_template('design/editor.html', stage='editing', image_url=url_for('static', filename='uploads/' + current_time + os.path.splitext(img.filename)[1]))
        except Exception as e:
            print(e)
            return render_template('design/editor.html', stage='upload')
    else:
        return render_template('design/editor.html', stage='upload')

if __name__ == '__main__':
    app.run(debug=True)