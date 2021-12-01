
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/receipt', methods=['POST'])
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
        return render_template('receipt.html')
        
    

app.run(debug=True)
    