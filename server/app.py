#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f"parameter received:{parameter}")
    return f'<h1>print: {parameter}</h1>'


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers  = [str(i) for i in range(parameter)]

    output = '<br>'.join(numbers)
    return f'<h1>count:{parameter}</h1><br>{output}'


@app.route('/math/int:num1/int:num2/<string:operation>')
def math(num1, num2, operation):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        return f'<h1> Invalid operation: {operation}</h1>'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
