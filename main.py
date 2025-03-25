import flask


# TODO: change this to your academic email
AUTHOR = "gkirsch@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    uppercase_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    special_characters = set("!@#$%^&*")

    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password under 8 characters"}), 400

    if not any(char in uppercase_letters for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one uppercase letter"}), 400

    if not any(char in digits for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one digit"}), 400

    if not any(char in special_characters for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one special character"}), 400

    

    # FIXME: to be implemented
    return flask.jsonify({"valid": True, "reason": "Valid password"}), 100
