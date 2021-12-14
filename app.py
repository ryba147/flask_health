from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    response = { "status": "ok" }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
