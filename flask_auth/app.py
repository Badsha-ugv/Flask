from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import  LoginManager, current_user, login_user, logout_user 
from flask_bcrypt import Bcrypt

from models import db, Todo, User 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'my secret key'


db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)


bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


# @app.route('/login/<id>')
# def login(id):
#     user = User.query.get(id)
#     login_user(user)
#     return 'success'

@app.route('/logout')
def logout():
    
    logout_user()
    return 'log out succes'


@app.route('/')
def index():
    
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return 'not loged in'
    

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        hash_pass = bcrypt.generate_password_hash(password)

        user = User(username=username, email=email, password=hash_pass)
        db.session.add(user)
        db.session.commit()
        print('register success')
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('register.html')
    
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter(User.username==username).first()
            print('user obj ',user)
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'password not matched!'
            
        except:
            return 'user not found!'




if __name__ == '__main__':
    app.run(debug=True)