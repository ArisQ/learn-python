#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def sign_in_form():
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return render_template('signin-ok.html', username=username)
    return render_template('signin.html', message='Authentication failed', username=username)


if __name__ == '__main__':
    app.run()
