from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about/')
def about():
    return '<h3>About Me</h3>'

@app.route('/user/<name>/')
def user(name):
    return f'I am {name}'

@app.route('/sum/<int:n1>/<int:n2>/')
def add_number(n1,n2):
    return f'Sum is {n1+n2}'

@app.route('/params/')
def param():
    data = request.args
    name = request.args['name']

    return f'{data['name']} { name}'

@app.route('/req', methods=['GET','POST'])
def req():
    if request.method == 'POST':
        return 'This is post request'
    return 'This is get request'

# curl -X get http://127.0.0.1:5000/route :) 
# curl -I -> get response header 

if __name__ == '__main__':
    app.run(debug=True)
