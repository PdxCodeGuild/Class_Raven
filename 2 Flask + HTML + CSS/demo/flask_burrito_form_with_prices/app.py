from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('./static/options.json', 'r') as json_file:
        data = json.loads(json_file.read())

    radio_categories = data['radio_categories']
    order_options = data['order_options']

    return render_template('index.html', radio_categories=radio_categories, order_options=order_options)




def field_data_to_dict(field_data):
    '''
    Convert field_data from  format to dictionary.
    ['veggies', '2.00'] => {'name': 'veggies, 'price':'2.00'}
    '''
    name, price = field_data
    
    return {
        'name': name,
        'price': price
    }


@app.route('/order', methods=['POST'])
def process_order():

    order_total = 0
    receipt = {}
    # process the form
    for field in request.form:
        if field == 'extra':
            # convert each extra item into a dictionary
            # ['cheese-1.00', 'sour cream-0.50'] -> [['cheese', '1.00'],['sour cream', '0.50']]
            field_data = [item.split('-') for item in request.form.getlist('extra')]
            
            # convert each split list into a dict
            # [{'name': 'cheese', 'price':'1.00}, {'name': 'sour cream', 'price': '0.50'}]
            field_data = [field_data_to_dict(item) for item in field_data]
        else:
            # value comes through as veggie-2.00. Split at the '-' is ['veggies', '2.00']
            field_data = request.form[field].split('-')

            # all fields other than 'delivery' will have 2 items
            if len(field_data) > 1:
                field_data = field_data_to_dict(field_data)
                
                # add price to total if it exists
                order_total += float(field_data['price'])

            else:
                # delivery will have a price of 0.00 which won't be displayed on the template
                field_data = field_data_to_dict([field_data[0],'0.00'])

        # add field data for the current field
        # {'protein': {'name': 'carne asada', 'price': '3.00'}}
        receipt[field] = field_data


    return render_template('receipt.html', receipt=receipt, order_total=order_total)
