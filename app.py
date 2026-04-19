from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/square", methods=["GET"])
def square():
    try:
        n = float(request.args.get("n"))
        return jsonify({"input": n, "result": n**2})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètre 'n' invalide ou manquant"}), 400


@app.route("/triple", methods=["GET"])
def square():
    try:
        n = float(request.args.get("n"))
        return jsonify({"input": n, "result": n**3})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètre 'n' invalide ou manquant"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
