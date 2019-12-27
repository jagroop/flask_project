from flask import render_template, request, session, redirect, url_for
from datetime import timedelta

from app import app

app.secret_key = 'l!k91^NpPqgs$4Y5xcMC'
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/login')
def login():
    if 'user' in session:
      return redirect(url_for('user'))
    else:
      return render_template("login.html")

@app.route('/user_login', methods=['POST'])
def user_login():
    username = request.form.get('username')
    session.permanent = True
    session['user'] = username
    return redirect(url_for('user'))

@app.route('/user')
def user():
  if 'user' in session:
    username = session['user']
    return render_template('user.html', username=username)
  else:
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session.pop('user', None)
  return redirect(url_for('login'))