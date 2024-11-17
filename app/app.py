from flask import Flask, render_template, request, redirect, url_for
import os

import database as db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('BIBDHEK_KEY')

@app.route('/books')
def books():
    books = db.books.get_all()
    return render_template('books.html', books=books)

@app.route('/loans')
def loans():
    loans = db.loans.get_open_loans()
    return render_template('loans.html', loans=loans)

@app.route('/users')
def users():
    users = db.users.get_all()
    return render_template('users.html', users=users)

@app.route('/add_book')
def add_book():
    return render_template('add_book.html')

@app.route('/add_user')
def add_user():
    return render_template('add_user.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
