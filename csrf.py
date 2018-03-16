#-*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
#CSRF跨站保护密匙
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template('user.html', name=name)
#404页面和500页面
@app.errorhandler(404)
def four
