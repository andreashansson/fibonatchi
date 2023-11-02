from flask import Flask, jsonify, request

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
        return jsonify({"message": "created successfully"}), 201

    @app.route("/skipped/<position>", methods=["DELETE"])
    def delete_skipped_position(position):
        return jsonify({"message": "removed successfully"}), 204

    def start(self):
        app.run(port=5005)
