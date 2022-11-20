from flask import render_template,request
from app.models import User
from flask import Flask
from app.adapters.db import Session, engine

app = Flask(__name__, template_folder='templates')

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
    return render_template('login.html')

app.run(debug=True)

