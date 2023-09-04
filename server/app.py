#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string>")
def print_string(string):
    print(string)
    return string


@app.route("/count/<int:integer>")
def count(integer):
    str = ""
    for i in range(0, integer):
        str += f"{i}\n"
    return str


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "div":
        operation = "/"
    return str(eval("{}{}{}".format(num1, operation, num2)))

if __name__ == '__main__':
    app.run(port=5555, debug=True)
