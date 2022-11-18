from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flaskpostgres:flask2022@postgres:5432/flaskdb'
# login_manager = LoginManager()
# login_manager.init_app(app)
db = SQLAlchemy(app)

