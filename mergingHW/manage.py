import os

from flask import Flask, render_template, redirect, url_for, request, send_file

from merge_files import *

app = Flask(__name__)


@app.route('/')
@app.route('/select_files')
def select_files():
    return render_template('select_files.html')


@app.route('/order_of_files', methods=['GET', 'POST'])
def order_of_files():
    filenames = get_all_files()
    return render_template('order_of_files.html', filenames=filenames)


@app.route('/concat_and_order', methods=['POST'])
def concat_and_order():
    filenames = request.form['filenames']
    filenames = filenames.split('/')
    # TODO: read and implement ordering
    concat_and_enumerate(filenames)
    return redirect(url_for('output'))


@app.route('/output')
def output():
    return render_template('output.html')


@app.route('/see_file')
def see_file():
    return send_file('./output/output.def', as_attachment=True)