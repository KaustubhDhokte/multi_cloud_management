import json
import api.operators.mcoperator as mcoperator
from flask_cors import CORS
from flask import Flask, request
from api.operators.mcoperator import Operator
from api.kinds.mckinds import CustomResource
from flask import Response


app = Flask(__name__)
CORS(app)


@app.route("/operator", methods=["POST"])
def register():
    """
    Register the operator
    """
    response_object = Response()
    try:
        request_body = request.json
        name = request_body["name"]
        install_commands = request_body["install_commands"]
    except KeyError as kex:
        response_object.response = "Missing field in JSON : " + kex
        response_object.status_code = 401
        return response_object
    try:
        uninstall_commands = request_body["uninstall_commands"]
        hub_link = request_body["link"]
    except Exception as ex:
        uninstall_commands = None
        hub_link = None
    try:
        oprtr = Operator(name, install_commands, hub_link, uninstall_commands)
        oprtr.register()
        response_object.response = "Registration Successful"
        response_object.status_code = 200
    except Exception as ex:
        response_object.response = f"Registration failed. {ex}"
        response_object.status_code = 500
    return response_object


@app.route("/operator/install/<name>", methods=["POST"])
def install_operator(name):
    """
    Install the operator
    """
    try:
        response = Response()
        oprtr = Operator(name)
        oprtr.install()
        response.data = name
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/operator/uninstall/<name>", methods=["POST"])
def uninstall_operator(name):
    """
    Uninstall the operator
    """
    try:
        response = Response()
        oprtr = Operator(name)
        oprtr.uninstall()
        response.data = name
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/operator/<name>", methods=["DELETE"])
def delete_operator(name):
    """
    Delete the operator
    """
    try:
        response = Response()
        oprtr = Operator(name)
        oprtr.delete()
        response.status_code = 204
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/operator")
def get_all_operators():
    """
    """
    try:
        response = Response()
        data = mcoperator.get_all_operators()
        response.data = json.dumps(data)
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/operator/<operator_name>")
def get_operator(operator_name):
    """
    """
    try:
        response = Response()
        oprtr = Operator(operator_name)
        operator_data = oprtr.get()
        response.data = json.dumps(operator_data)
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource", methods=["POST"])
def create_resource():
    """
    Create instance
    """
    try:
        response = Response()
        request_body = request.json
        kind = request_body["kind"]
        resource_name = request_body["metadata"]["name"]
        crd = CustomResource(resource_name, kind, request_body)
        crd.create(request_body)
        response.data = resource_name
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource/<resource_name>", methods=["PUT"])
def update_resource(resource_name):
    """
    Update instance
    """
    try:
        response = Response()
        request_body = request.json
        crd = CustomResource(resource_name)
        crd.update(request_body)
        response.data = resource_name
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource")
def get_all_resources():
    """
    """
    try:
        response = Response()
        response.data = "getall success"
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource/<resource_name>")
def get_resource(resource_name):
    """
    """
    try:
        response = Response()
        crd = CustomResource(resource_name)
        response.data = json.dumps(crd.get())
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource/deploy", methods=["POST"])
def deploy_resource():
    """
    Create resource instance
    """
    try:
        response = Response()
        request_body = request.json
        name = request_body["name"]
        crd = CustomResource(name)
        response.data = crd.deploy()
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


@app.route("/resource/<name>", methods=["DELETE"])
def delete_resource(name):
    """
    Create resource instance
    """
    try:
        response = Response()
        crd = CustomResource(name)
        response.data = crd.delete()
        response.status_code = 200
    except Exception as ex:
        response.data = ex
        response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
