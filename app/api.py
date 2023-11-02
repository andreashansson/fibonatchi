from flask import Flask, jsonify, request

app = Flask(__name__)

class Api:
    def __init__(self):
        pass

    @app.route("/positions/<position>")
    def positions(position):
        if request.args.get('fetch') == "one":
            print("fetch given number")
        else:
            print("fetch all up to given number")

        return jsonify({})

    @app.route("/skipped", methods=["POST"])
    def add_skipped_position():
        return jsonify({"message": "created successfully"}), 201

    @app.route("/skipped/<position>", methods=["DELETE"])
    def delete_skipped_position(position):
        return jsonify({"message": "removed successfully"}), 204

    def start(self):
        app.run(port=5005)
