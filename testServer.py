from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
	name = request.args.get('name')
	message = 'Hello, ' + name + '!'
	return message

# browse to localhost:8000/?name=William
app.run('0.0.0.0', port=8000, debug=True)