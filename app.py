from flask import Flask, request, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_numbers():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return a, b


@app.route('/add', methods=['GET'])
def add_route():
    a, b = get_numbers()
    result = add(a, b)
    return jsonify({'a': a, 'b': b, 'operation': 'addition', 'result': result})


@app.route('/subtract', methods=['GET'])
def subtract_route():
    a, b = get_numbers()
    result = subtract(a, b)
    return jsonify({'a': a, 'b': b, 'operation': 'subtraction', 'result': result})


@app.route('/multiply', methods=['GET'])
def multiply_route():
    a, b = get_numbers()
    result = multiply(a, b)
    return jsonify({'a': a, 'b': b, 'operation': 'multiplication', 'result': result})


@app.route('/divide', methods=['GET'])
def divide_route():
    a, b = get_numbers()
    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    result = divide(a, b)
    return jsonify({'a': a, 'b': b, 'operation': 'division', 'result': result})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
