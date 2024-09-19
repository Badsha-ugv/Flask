from flask import Flask, render_template, session, make_response, request

app = Flask(__name__)
app.secret_key = 'my secret key'


@app.route('/')
def index():
    return render_template('index.html', msg='Hello world')


@app.route('/set-session')
def set_session():
    session['name'] = 'jhon'
    session['type'] = 'admin'

    return render_template('index.html', msg='session set')

@app.route('/get-session')
def get_session():
    if 'name' in session.keys() and 'type' in session.keys():
        name = session['name'] 
        type =  session['type']
        return render_template('index.html', msg=f'session value {name} {type}')
    else:
        return render_template('index.html', msg=f'no session value found')
        
@app.route('/clear-session')
def clear_session():
    session.clear()
    return render_template('index.html', msg=f'session value is clear')



@app.route('/set-cookie')
def set_cookie():
    response = make_response(render_template('index.html',msg='cookie is set'))
    response.set_cookie('user_cookie','user_cookie_value')
    return response 

@app.route('/get-cookie')
def get_cookie():
    if 'user_cookie' in  request.cookies.keys():
        cookie_val = request.cookies['user_cookie']
        return render_template('index.html', msg = f'cookie value is {cookie_val}') 
    else:
        return render_template('index.html', msg = f'cookie value is empty') 

@app.route('/clear-cookie')
def clear_cookie():
    response = make_response(render_template('index.html',msg='cookie is removed'))
    response.set_cookie('user_cookie', expires=0)
    return response 