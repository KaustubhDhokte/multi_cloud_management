"""
"""
from .mcoperator import Operator
from ...server import app as app
import json

#@app.route("/operator", methods=["POST"])
@app.route("/operator")
def operator_register():
    """
    """
    print(json.loads(request.data))