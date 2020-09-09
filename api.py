from flask import Flask, request, jsonify

from colleges_script import get_colleges

app = Flask(__name__)


@app.route("/api/v1/colleges/list", methods=['POST'])
def run_colleges_script():
    data = request.json
    return get_colleges(data)