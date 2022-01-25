from flask import Flask, request
from flask import render_template as render

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    groups = ['tortilla', 'meat', 'rice', 'beans', 'cheese', 'sour cream']
    group_options = {
        'tortilla': {
            'choices': ['flour', 'corn', 'wheat', 'spinach']
            },
        'meat': {
            'choices': ['beef', 'chicken', 'pork', 'none']
            },
        'rice': {
            'choices': ['white', 'brown']
            },
        'beans': {
            'choices': ['black', 'pinto']
            },
        'cheese': {
            'choices': ['si', 'no']
            },
        'sour cream': {
            'choices': ['si', 'no']
            }

    }
    if request.method == 'POST':
        order = request.form
        return render('order.html', order=order)

    return render('index.html', groups=groups, group_options=group_options)
