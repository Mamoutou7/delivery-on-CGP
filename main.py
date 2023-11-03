"""
Created by Mamoutou Fofana
November, 3, 2023

"""
from flask import Flask
from flask import jsonify

app = Flask(__name__)



employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route('/')
def hello_world():
    """Return a friendly HTTP greeting."""
    return 'Hello World I am building AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)