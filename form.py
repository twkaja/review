# -*- coding:utf-8 -*-

from flask import Flask, render_template, redirect, url_for, session, flash
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os

#sqlite数据库
from flask_sqlalchemy import SQLAlchemy

#存放数据库的文件夹
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a hard string to guess'
#配置数据库的绝对地址
app.config['SQLALCHEMY_DATABASW_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    #自动提交

manager = Manager(app)
db = SQLAlchemy(app)

#表单类
class NameForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired(), ])
    submit = SubmitField('Submit')
#定义模型
class Role(db.Model):
    #表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    #有了backref，往User中添加了一个role属性，使得User实例可以是这样访问,user.role
    #而不是使用role_id访问
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role {}>'.format(self.name)
    
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    #这列的值是roles表中的id
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.uername)
    



    

@app.route('/', methods=['GET', 'POST'])
def index():
    #重定向
    form = NameForm()

    if form.validate_on_submit():
        #flash消息
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)
    
@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run()
