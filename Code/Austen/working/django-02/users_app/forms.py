from django.forms import Form, CharField, PasswordInput, EmailInput


class LoginForm(Form):
    username = CharField(label='Username', max_length=20)
    password = CharField(label='Password', max_length=20,
                         min_length=8, widget=PasswordInput)


class RegisterForm(Form):
    first_name = CharField(label='First Name')
    last_name = CharField(label='Last Name')
    email = CharField(label='email address', widget=EmailInput)
    username = CharField(label='Username', max_length=20)
    password = CharField(label='Password', max_length=20,
                         min_length=8, widget=PasswordInput)
    confirm = CharField(label='Confirm password', max_length=20,
                        min_length=8, widget=PasswordInput)
