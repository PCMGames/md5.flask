import flask, hashlib

app = flask.Flask(__name__)

OurGithub = "https://github.com/"

@app.route("/")
def main():
    return f'<meta http-equiv="refresh" content="0; URL={OurGithub}" />'

@app.route("/encode/<string>")
def encode(string):

    result = hashlib.md5(string.encode())

    return str(result.hexdigest())

app.run(debug=False, host="0.0.0.0", port=25566)
