from flask import jsonify, render_template

from flask_health import app


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/health')
def health():
    response = {"status": "ok"}
    return jsonify(response)


"""
patients and hospitals packages with blueprint
models with schemas
views with logic

"""
