# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
	
@app.route('/fawad')
def hello_world():
    return 'Hello fawad!'

if __name__ == '__main__':
    app.run()

