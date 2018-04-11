#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1><p><a href="/signin">Sign In</a></p>'


@app.route('/signin', methods=['GET'])
def sign_in_form():
    return '''<h1><a href="/">Home</a></h1>
    <form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''


@app.route('/signin', methods=['POST'])
def sign_in():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return '<h3>Hello, Administrator!</h3><p><a href="/signin">Back</a></p>'
    return '<h3>Authentication failed.</h3><p><a href="/signin">Back</a></p>'


if __name__ == '__main__':
    app.run()
