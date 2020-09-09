from flask import Flask, request, jsonify

from colleges_script import get_colleges

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello! This API is managed by CARMSNawaz'


@app.route("/api/v1/colleges/list", methods=['POST'])
def run_colleges_script():
    data = request.json
    return jsonify(get_colleges(data))
