import os

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/select_files')
def select_files():
    return "hello world"


@app.route('/order_of_files')
def order_of_files():
    return "Determine the order of concatenation"


@app.route('/concat_and_order')
def concat_and_order():
    return "here is your .def file"