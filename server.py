import json
from flask_cors import CORS
from flask import Flask, request
from api.operators.mcoperator import Operator

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    """
    abc
    """
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/operator", methods=["POST"])
def register():
    """
    register
    """
    request_body = request.json
    name = request_body["name"]
    install_commands = request_body["install_commands"]
    uninstall_commands = request_body["uninstall_commands"]
    hub_link = request_body["link"]
    oprtr = Operator(name, install_commands, link)
    oprtr.register()
    return 

if __name__ == "__main__":
    app.run(host='0.0.0.0')