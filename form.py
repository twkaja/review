# -*- coding:utf-8 -*-

from flask import Flask, render_template, redirect, url_for
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
manager = Manager(app)

app.config['SECRET_KEY'] = 'a hard string to guess'

#表单类
class NameForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired(), ])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = NameForm()
    if form.validate_on_submit():
        return render_template('index.html', name=form.name.data, form=form)
    else:
        return render_template('index.html', name=None, form=form)
@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run()
