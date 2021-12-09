from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('lab-06.html')

@app.route('/results', methods=['GET', 'POST'])
def calculate():
    user_distance=float(request.form['user_distance'])
    user_unit=request.form['user_unit']
    output_unit=request.form['output_unit']
    print(f"{user_distance} {user_distance} {user_distance}")
    conversion_factor ={'ft':0.3048, "mi":1609.34, "m":1, "km":1000, "in":0.0254, "yd":0.9144}
    output = user_distance * conversion_factor[user_unit]
    final_output = output / conversion_factor[output_unit]
    print(final_output)
    return render_template('lab-06.html', final_output=final_output, output_unit=output_unit)
