import random
from flask import Flask, jsonify

app = Flask(__name__)

def return_zuzu():
	zuzus = random.randint(1,10)
	times = random.randint(1,10)
	zuzu = "zu"*times
	for i in range(zuzus-1):
		times = random.randint(1,10)
		zuzu += " "+("zu"*times)
	return zuzu


@app.route("/")
def hello():
	return_zuzu()

@app.route("/api")
def api():
	api_return = {"zuzu_text":return_zuzu()}
	return jsonify(api_return)

if __name__ == '__main__':
	app.run()