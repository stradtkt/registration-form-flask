from flask import Flask, render_template, redirect, request, flash, session
import re
app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

@app.route('/')
def index():
  return render_template('contact.html')


@app.route('/result', methods=['POST'])
def result():
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['password'] = request.form['password']
  session['confirm'] = request.form['confirm_password']
  validation_error = False

  if len(session['first_name']) < 2:
    flash("Please enter a longer first name")
    validation_error = True
  elif len(session['first_name']) > 40:
    flash("Please enter a shorter first name")
    validation_error = True

  if len(session['last_name']) < 2:
    flash("Please enter a longer last name")
    validation_error = True
  elif len(session['last_name']) > 60:
    flash("Please enter a shorter last name")
    validation_error = True

  EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

  if not EMAIL_REGEX.match(session['email']):
    flash("Please enter a valid email address")
    validation_error = True

  if len(session['password']) < 5:
    flash("Enter a longer password")
    validation_error = True
  elif len(session['password']) > 30:
    flash("Please enter a short password so you will remember it!")
    validation_error = True

  if session['confirm'] != session['password']:
    flash("Confirm password does not match with the first password, please enter it again!")
    validation_error = True

  if validation_error == True:
    return redirect('/')
  else:
    return render_template('result.html')


app.run(debug=True)