#-*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello tangwei'
#动态路由
#路由名称最好和视图函数名相同
@app.route('/user/<name>')
def user(name):
    return 'hello {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
