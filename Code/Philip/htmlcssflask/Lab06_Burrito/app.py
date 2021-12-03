# app.py 
from flask import Flask, render_template, request

app = Flask(__name__)

# home route
@app.route("/")
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_data():
    '''result=request.form'''
    name=request.form['name']
    tortilla=request.form['tortilla']
    rice=request.form['rice']
    beans=request.form['beans']
    protein=request.form['protein']
    cheese=request.form['cheese']
    sourcream=request.form['sourcream']
    delivery_instructions=request.form['deliveryinstructions']
   
    return render_template('receipt.html', name=name, delivery_instructions=delivery_instructions, tortilla=tortilla, rice=rice, beans=beans, protein=protein, cheese=cheese, sourcream=sourcream)
    
    
    



app.run(debug = True) 
