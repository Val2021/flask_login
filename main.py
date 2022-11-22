from flask import render_template,request,redirect, url_for
from app.models import User, Base
from flask import Flask
from app.adapters.db import Session, DATABASE_URL
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from flask_login import login_user, LoginManager
from app.repositories.base_repository import BaseRepository
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__, template_folder='templates')
app.debug = True
app.secret_key = 'xxxxyyyyyzzzzz'
login_manager = LoginManager()
login_manager.init_app(app) 
login_manager.login_view = 'login'

LOGGER = logging.getLogger(__name__)

engine = _sql.create_engine(DATABASE_URL)
postgres = BaseRepository(
    session=_orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )(),
    model=User,
)
Base.metadata.create_all(engine)

@login_manager.user_loader
def load_user(email):
    return postgres.get_login_email(email)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name,email,pwd)

        db = Session()
        db.add(user)
        db.commit()
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = postgres.get_login_email(email=email)

        LOGGER.info(user)

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)

