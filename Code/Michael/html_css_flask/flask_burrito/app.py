from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_data(filename):
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())

def write_data(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))
    return

JSON_DATA = './static/data.json'

@app.route('/')
def index():
    order = get_data(JSON_DATA)
    return render_template('index.html', order=order)

@app.route('/order', methods=['GET','POST'])
def order():
    if request.method == 'POST':
        order = get_data(JSON_DATA)
        
        new_order = {
            'order_id': len(order) + 1,
            'name': request.form['name'],
            'tortilla': request.form['tortilla'],
            'rice': request.form['rice'],
            'beans': request.form['beans'],
            'protein': request.form['protein'],
            'extra': request.form.getlist('extra'),
            'deliveryInstructions': request.form['deliveryInstructions']
        }
        
        order.insert(0, new_order)
        
        
        write_data(JSON_DATA, order)
        return redirect(url_for('receipt', order_number=new_order['order_id']))
    else:
        return render_template('order.html')
    
@app.route('/receipt/<int:order_number>')
def receipt(order_number):
    orders = get_data(JSON_DATA)
    
    for i in range(len(orders)):
        order = orders[i]
        
        if order['order_id'] == order_number:
            break
    
    return render_template('receipt.html', order=order)

