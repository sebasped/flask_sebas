from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, World! en hello!'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)
