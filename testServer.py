from flask import Flask, request
app = Flask(__name__)

@app.route('/reverse/<word>')
def index(word):
	return word[::-1]

# browse to localhost:8000/?name=William
app.run('0.0.0.0', port=8000, debug=True)
