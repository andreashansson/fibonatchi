from flask import Flask, jsonify

app = Flask(__name__)

class Api:
    def __init__(self):
        pass

    @app.route("/positions/<position>")
    def positions(position):
        return jsonify({})

    @app.route("/skipped", methods=["POST"])
    def add_skipped_position():
        return jsonify({"message": "created successfully"}), 201

    @app.route("/skipped/<position>", methods=["DELETE"])
    def delete_skipped_position(position):
        return jsonify({"message": "removed successfully"}), 204

    def start(self):
        app.run(port=5005)
