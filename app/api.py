from flask import Flask, jsonify, request
from fibonatchi import Fibonatchi, WrongInputError

app = Flask(__name__)
fc = Fibonatchi("./app/skipped.json")

class Api:
    def __init__(self):
        pass

    @app.route("/positions/<position>")
    def positions(position):
        try:
            if request.args.get('fetch') == "one":
                res = fc.get_fib_val_by_fib_pos(position)
            else:
                res = fc.get_fib_vals_up_to_fib_pos(position)
        except WrongInputError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify(res), 200

    @app.route("/skipped", methods=["POST"])
    def add_skipped_position():
        position = request.get_json().get("position")
        if not position:
            return jsonify({"message": "no value in position body"}), 400

        try:
            fc.set_vals_to_skip(position)
        except WrongInputError as e:
            return jsonify({"message": str(e)}), 400

        return jsonify({"message": "added successfully"}), 201

    @app.route("/skipped/<position>", methods=["DELETE"])
    def delete_skipped_position(position):
        fc.remove_skipped_val(position)
        return jsonify({"message": "removed successfully"}), 204

    def start(self):
        app.run()
