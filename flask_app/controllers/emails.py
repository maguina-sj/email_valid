from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email']
    }
    Email.save(data)
    return redirect ('/success')
    

@app.route('/success')
def success():
    return render_template('success.html', allemails=Email.getAll())

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/success')