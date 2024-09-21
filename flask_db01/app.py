from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# setup app 
app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# setup db 
db = SQLAlchemy(app)

# migrate db
migrate = Migrate(app, db)

# db model
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.title}'


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/create',methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        task = Task(title=title,desc=desc)
        db.session.add(task)
        db.session.commit()
        return redirect('/')


# run server 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()



'''
cmd: 
flask db init
flask migrate
flask upgrade

'''