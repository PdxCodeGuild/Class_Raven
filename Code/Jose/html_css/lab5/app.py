from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def create_receipt():

    receipt = {
        'tortilla': request.form['tortilla'],
        'protein': request.form['protein'],
        'rice': request.form['rice'],
        'beans': request.form['beans'],
        'extra': request.form.getlist('extra'),
    }

    return render_template('receipt.html', receipt=receipt)

app.run(debug = True) 