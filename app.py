import datetime
import json
import os.path
from fileinput import filename
from traceback import print_tb

from flask import Flask, render_template, request, url_for, jsonify
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


@app.route('/order', methods=['POST', 'GET'])
def order():
    with databaseHandler() as db:
        return render_template('order/order.html', phone_models=db.getPhoneModels())

@app.route('/design', methods=['POST', 'GET'])
def design():
    if request.method == 'POST':
        model_json = request.form.get('model')
        model = json.loads(model_json)
        return render_template('design/design.html', model=model, stage='upload')
    return None


@app.route('/refresh-editor', methods=['POST', 'GET'])
def refreshEditor():
    if request.method == 'POST':
        try:
            img = request.files['img']
            model_received = json.loads(request.form.get('model'))
            if img.filename is not None and model_received is not None:
                with databaseHandler() as db:
                    current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], current_time + os.path.splitext(img.filename)[1])
                    img.save(filepath)

                    template = db.getOnePhoneTemplate(model_received['id'])

                    return jsonify({
                        'image_url': url_for('static', filename='uploads/' + current_time + os.path.splitext(img.filename)[1]),
                        'model_template': url_for('static', filename='templates/' + template)
                    })
        except Exception as e:
            print(e)
            return render_template('design/editor.html', stage='upload')
    else:
        return render_template('design/editor.html', stage='upload')

if __name__ == '__main__':
    app.run(debug=True)