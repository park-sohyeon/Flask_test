from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(__name__)
    return 'Hello World'

@app.route('/one')
def hello_one():
    return 'Hello one'

@app.route('/two')
def hello_two():
    return 'Hello two'

if __name__== '__main__':
    app.run(host = '0.0.0.0')

