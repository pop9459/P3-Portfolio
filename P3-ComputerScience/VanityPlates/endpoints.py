from flask import Flask, jsonify, request
from db_handler import *
from plate_checker import *

# ##### Object initialization #####
flask_api = Flask(__name__)

# ##### Define the API endpoints #####
@flask_api.get("/")
def index():
    return jsonify({"message": "Vanity plate API is running"})

@flask_api.post("/validate")
def validate_plate():
    # Get the JSON data from the request.
    data = request.get_json(silent=True) or {}
    plate = data.get("plate", "")

    if not isinstance(plate, str):
        return jsonify({"error": "'plate' must be a string"}), 400

    return jsonify({
        "plate": plate,
        "valid": is_valid(plate)
    })

@flask_api.post("/register")
def register_plate():
    # Get the JSON data from the request.
    data = request.get_json(silent=True) or {}
    plate = data.get("plate", "")

    if not isinstance(plate, str):
        return jsonify({"error": "'plate' must be a string"}), 400

    if not is_valid(plate):
        return jsonify({
            "plate": plate,
            "inserted": False,
            "reason": "Invalid plate format"
        }), 400
    
    if not add_plate_to_db(plate):
        return jsonify({
            "plate": plate,
            "inserted": False,
            "reason": "Plate already registered"
        }), 400
    
    return jsonify({
        "plate": plate,
        "inserted": True
    })

@flask_api.get("/plates")
def list_plates():
    return jsonify({"plates": get_registered_plates()})