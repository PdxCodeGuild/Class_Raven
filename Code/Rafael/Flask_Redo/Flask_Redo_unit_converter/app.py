from flask import Flask, render_template, url_for


app = Flask(__name__)

# render to the page specified


@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)


@app.route('/', methods=['POST'])
def answer(): 
    
    meters_convert = {
    'ft': 0.3048,
    'm': 1,
    'km': 1000,
    'mi': 1609.34
    }

    i = 0

    while i == 0:

        q1 = int(input('What is the distance in meters? '))

        q2 = (input('what are the units?; ft, m, km, mi: '))

        total = q1 * meters_convert[q2]

        print(total, 'meters')

    #else: 
            #print('Try again, select either miles: "mi", meters: "m", kilometers: "km" or feet: "ft" after entering a distance')
        break                           

    return render_template('index.html', total=total)

#runs Flask automatically at start
if __name__ == '__main__':
   app.run()