from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    # to generate each card
    radio_categories = ['tortilla', 'rice', 'beans', 'protein']

    # to generate the content for each card
    order_options = {
        'tortilla': {
            'choices': ['white flour', 'wheat flour', 'corn', 'spinach'],
            'image_url': 'images/tortilla.webp'
        },
        'rice': {
            'choices': ['white', 'brown'],
            'image_url': 'images/rice.webp'
        },
        'beans': {
            'choices': ['black', 'pinto', 'refritos'],
            'image_url': 'images/beans.webp'
        },
        'protein': {
            'choices': ['carne asada', 'pollo', 'carnitas', 'sofritas', 'veggies'],
            'image_url': 'images/meat.webp'
        },
        'extra': {
            'choices': ['cheese', 'sour cream'],
            'image_url': ''
        }
    }

    return render_template('index.html', radio_categories=radio_categories, order_options=order_options)



@app.route('/order', methods=['POST'])
def process_order():

    receipt = {
        'tortilla': request.form['tortilla'],
        'rice': request.form['rice'],
        'beans': request.form['beans'],
        'protein': request.form['protein'],
        'extra': request.form.getlist('extra'), # find all fields with name 'extra' and make a list
        'delivery': request.form['delivery']
    }

    return render_template('receipt.html', receipt=receipt)