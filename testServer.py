from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/reverse/<word>')
def _reverse(word):
	return word[::-1]

@app.route('/random/<int:quantity>')
def _random(quantity):
	response = []
	for i in range(quantity):
		response.append(random.randint(0, 100))
	return ' '.join(map(str, response))

# browse to localhost:8000/?name=William
app.run('0.0.0.0', port=8000, debug=True)
