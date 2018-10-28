from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('sign_up_form.html')


@app.route("/", methods=['POST'])
def welcome():
    username = request.form.get('username')
    password = request.form.get('password')
    verify = request.form.get('verify')
    email = request.form.get('email')
    
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a vaild username"
    if password == '' or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "That's not a vaild password"
    if verify == '' or len(verify) < 3 or len(verify) > 20 or ' ' in verify:
        verify_error = "That's not a vaild password"
    elif password != verify:
        verify_error = "Passwords don't match"
    if email == '':
        email=email
    elif not '@' in email:
        email_error = "That's not a vaild email"
    elif not '.' in email:
        email_error = "That's not a vaild email"
    elif len(email) < 3 or len(email) > 20 or ' ' in email:
        email_error = "That's not a vaild email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', title='Signup', username=username) 
    else:
        return render_template('sign_up_form.html', title='Signup', 
            username_error=username_error, 
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error,
            username=username,
            email=email)

app.run()