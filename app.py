from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return jsonify({"para": "de crashar"})


if __name__ == '__main__':
    app.run()
