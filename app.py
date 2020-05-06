from flask import Flask, render_template

app = Flask(__name__)  # name the application app after the file


@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo1'
    }, {
        'description': 'Todo2'
    }, {
        'description': 'Todo3'
    }])
