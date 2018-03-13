#-*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    manager.run()
