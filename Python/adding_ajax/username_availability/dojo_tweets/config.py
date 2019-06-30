from flask import Flask		# same as beforecopy
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from flask_migrate import Migrate			# this is new
from flask_bcrypt import Bcrypt       

app = Flask(__name__)
app.secret_key = "super secret"

# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojo_tweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)

# an instance of the ORM
db = SQLAlchemy(app)

# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)
