from flask import Flask, render_template, flash, request, redirect
app = Flask(__name__)
app.secret_key = 'my secret'


@app.route('/')
def index():
   
    return render_template('flashmsg.html')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            flash('login success')
            return redirect('/')
        else:
            flash('lgin failed')
            return redirect('/')
