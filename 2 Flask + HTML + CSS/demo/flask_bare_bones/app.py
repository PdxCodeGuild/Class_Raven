from flask import Flask, render_template, request
import json

# create the Flask app
app = Flask(__name__)

# set up an index route (home page).
# The slash '/' is the additional path off of 127.0.0.1:5000/localhost:5000
# in this case, localhost:5000/ will render the home page
@app.route('/')
def index():
    # index is the name of the view function that 
    # will be run when localhost:5000/ is visited

    # some values to render on the template
    first_name = 'Keegan'
    address = {
        'street': '123 Faux St',
        'city': 'Portland',
        'state': 'Oregon',
        'zipcode': '123456'
    }

    # Whatever is returned from this function will
    # be rendered by the browser as the HTTP response
    # Try the following return values:
    # return 'Hello world' # renders a string
    # return json.dumps(address) # renders the dictionary as a string
    # return '<h1 style="font-size: 200px;">Hello world!</h1>' # returns a single string of HTML
    
    # render_template() returns a string of HTML with any additional values inserted
    # additional values are provided as keyword arguments
    # template names are relative to the templates/ folder
    return render_template('index.html')



# the 'methods' argument can be provided to specify
# a list of allowed HTTP requests for the route
@app.route('/process', methods=['POST'])
def process_form():

    # the request object importe from Flask gives
    # access to the form data when this route is visited
    # if the text "I don't like spam!" was submitted with the form, 
    # the request.form object will look like this:
    # print(request.form) # ImmutableMultiDict([('text', "I don't like spam!")])

    # the request.form object can be used like a dictionary
    text = request.form['text']

    # render the template with the text
    # text=text translates to variable_on_template=data_from_view
    return render_template('display-output.html', text=text)


