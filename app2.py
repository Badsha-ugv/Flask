from flask import Flask, request, render_template, redirect, url_for 

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Badsha'
    return render_template('index.html',name=name)

# custom filter
@app.template_filter('reverse_str')
def rev(s):
    return s[::-1]


# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

@app.route('/profile')
def profile():
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)