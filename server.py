from flask import Flask, jsonify, request
import random
app = Flask(__name__)

#### REMINDER: The /double function will at random return a wrong result, as expected

@app.route("/double", methods=["POST"])
def double_number():
    r = request.get_json()

    try:
        number = r["number"]
    except (KeyError, TypeError):
        return jsonify({"error": "no number passed"}), 400

    try:
        if random.random() < 0.9:
            double = int(number)*2
        else:
            return random.randint(0,100)
    except ValueError:
        return jsonify({"error": "a number was not passed"}), 400

    return jsonify({"double": double}), 200
