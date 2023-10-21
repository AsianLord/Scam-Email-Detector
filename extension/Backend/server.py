from flask import Flask

app = Flask(__name__)

@app.route("/") # ‘https://www.google.com/‘

def home():
	text = 'Hello, world!'
	return text

app.run(port=5000)