#-*- coding:utf-8 -*-
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'welcome to this page'

if __name__ == '__main__':
    manager.run()
