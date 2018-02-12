#!/usr/bin/env python
#James Parks
#09/20/17

import os

import forms
from functools import wraps
from flask import Flask, g, render_template, Response, redirect, url_for, request

import bot
import user

app = Flask(__name__)
app.config.from_object('config')

root = os.getcwd()

current_user = user.User()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #if current_user.name is None:
        if g.user:
            return redirect(url_for('login')) #, next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/index')
#@login_required
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    #Make both motors go forward
    return

@app.route('/backward')
def backward():
    #Make both motors go backward
    return

@app.route('/left')
def left():
    #Make tank rotate left
    return

@app.route('/right')
def right():
    #make tank rotate right
    return

@app.route('/claw_close')
def claw_close():
    #make claw close
    return

@app.route('/claw_open')
def claw_open():
    #make claw open
    return

@app.route('/claw_toggle')
def claw_toggle():
    #toggle the state of the claw
    return

@app.route('/light_on')
def light_on():
    #turn headlight on
    return

@app.route('/light_off')
def light_off():
    #turn headlight off
    return

@app.route('/light_toggle')
def light_toggle():
    #toggle the state of the headlight
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

