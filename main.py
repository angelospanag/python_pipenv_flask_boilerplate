from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    response = dict()
    response['response'] = 'Hello World!'
    return jsonify(response), 200
