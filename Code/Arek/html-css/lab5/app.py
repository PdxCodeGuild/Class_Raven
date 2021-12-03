
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/receipt', methods=['GET', 'POST'])
def create_receipt():
    if request.method == 'POST':
        print(request.form)
        
        items = {
            'first-name': request.form['f-name'],
            'last-name': request.form['l-name'],
            'tortilla': request.form['tortilla'],
            'rice': request.form['rice'],
            'beans': request.form['beans'],
            'protein': request.form['protein'],
            'extra': request.form['extra'],
            'deliver': request.form['deliv-instructions']
        }
    return render_template('receipt.html', items=items) # this returns a 405 error if each button is not selected.
        
    

app.run(debug=True)
    