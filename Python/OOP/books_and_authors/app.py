#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import Flask, render_template,request,redirect			# same as beforecopy
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_and_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

books_authors_table = db.Table('books_authors',
                      db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
                      db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True))

class Book(db.Model):
  __tablename__ = "books"
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
  authors_who_wrote_book = db.relationship('Author',secondary=books_authors_table)

class Author(db.Model):
  __tablename__ = "authors"
  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))
  notes = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
  books_written_by_author = db.relationship('Book',secondary=books_authors_table)  
 
@app.route('/')
def index():
  all_books = Book.query.all()
  return render_template('add_book.html', all_books = all_books)

@app.route('/add_book', methods=["POST"])
def add_book():
  #get form inputs
  instance_of_book = Book(
    title = request.form['title'],
    description = request.form['description']
  )
  print(instance_of_book)
  db.session.add(instance_of_book)
  db.session.commit()
  return redirect('/')

  
@app.route('/authors')
def authors():
  all_authors = Author.query.all()
  return render_template('add_author.html', all_authors = all_authors)

@app.route('/add_author', methods=["POST"])
def add_author():
  #get form inputs
  instance_of_author = Author(
    first_name = request.form['first_name'],
    last_name = request.form['last_name'],
    notes = request.form['notes']
  )
  print(instance_of_author)
  db.session.add(instance_of_author)
  db.session.commit()
  return redirect('/authors')

@app.route('/books/<id>')
def view_book(id):
  book = Book.query.get(id)
  authors = book.authors_who_wrote_book
  all_authors = Author.query.all()
  return render_template('books.html', book = book, authors = authors, all_authors = all_authors)

@app.route('/add_authors_to_book', methods=["POST"])
def add_author_to_book():
  author_id = request.form['author_to_add']
  book_id = request.form['book_id']
  book = Book.query.get(book_id)
  author = Author.query.get(author_id)
  book.authors_who_wrote_book.append(author)
  db.session.commit()
  return redirect('/books/'+str(book_id))

@app.route('/authors/<id>')
def view_author(id):
  author = Author.query.get(id)
  books = author.books_written_by_author
  all_books = Book.query.all()
  return render_template('authors.html', books = books, author = author, all_books = all_books)

@app.route('/add_books_to_author', methods=["POST"])
def add_books_to_author():
  author_id = request.form['author_id']
  book_id = request.form['book_to_add']
  book = Book.query.get(book_id)
  author = Author.query.get(author_id)
  book.authors_who_wrote_book.append(author)
  db.session.commit()
  return redirect('/authors/'+str(author_id))


if __name__ == "__main__":
  app.run(debug=True)
