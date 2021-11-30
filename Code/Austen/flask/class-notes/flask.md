# Flask
## Setup
Flask is a python lib to render html templates
### Install
install pip3 install flask
### File Structure
> project-folder
>> `app.py`
>>
>
>> templates
>>> `index.html`

## Writing Flask Files
### `app.py`
1. import Flask
```
from flask import Flask
app = Flask(__name__)
```
2. identify page route
```
> @app.route('/')
# = domain.com/
> @app.route('/posts/<int:post_id>')
# = domain.com/posts/{post_id} ONLY if post_id == int()
```
3. create a function for the template
```
> def index():
# = the content rendered @ domain.com/
> def post(post_id):
# = the content rendered @ domain.com/posts/{post_id}
```
4. return page content to be rendered
```
# can return a string
>>    return 'Hello, World!'

# f-string
>>    return f'Showing post {post_id}'

# template stored with a file
>>    return render_template('index.html', name=name)

# name=name finds a variable stored in html `<h1> hello {{name}}</h1>` and replaces it with a variable stored in python `name = 'Your-Name'`
```
5. initiate debugging tools (disable before production)
```
app.run(debug=True)
```