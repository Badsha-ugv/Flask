from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        
        if 'username' in request.form.keys() and 'password' in request.form.keys():
            username = request.form['username']
            password = request.form['password']

            print(username, password)
            if username == 'admin' and password == 'admin':
                return 'Login Success' , 200
            else:
                return 'Invalid Credentials' , 404

@app.route('/upload-file', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        return file.read()


@app.route('/json-request', methods=['POST','GET'])
def json_req():
    if request.method == 'POST':
        title = request.json['title']
        desc = request.json['desc']
        data = jsonify({'title':title,'desc':desc})
        return data 
    else:
        return render_template('other.html')