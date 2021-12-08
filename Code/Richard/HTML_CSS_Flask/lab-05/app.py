from flask import Flask, request, render_template
from flask.wrappers import Request
app= Flask(__name__)

@app.route('/')
def burrito_form():
    return render_template('lab-05.html')

@app.route('/create', methods=['GET', 'POST'])
def burrito_order():
    print(request.form)
    # context={
    #     'name':request.form['name'],
    #     'tortilla':request.form['tortilla'],
    #     'rice':request.form['rice'],
    #     'beans': request.form['beans'],
    #     'protein':request.form['protein'],
    #     'additional_ingredients1':'',
    #     'additional_ingredients2':'',
    #     'delivery':'none'
    # }
    context={
        'name':request.form['name'],
        'tortilla':request.form['tortilla'],
        'rice':request.form['rice'],
        'beans': request.form['beans'],
        'protein':request.form['protein'],
        'additional_ingredients':request.form.getlist('additional_ingredients'),
        'delivery':request.form['delivery']
    }
    #print(context.values()
    return render_template('lab-05-receipt.html', context=context)