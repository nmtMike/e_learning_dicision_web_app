import os
from forms import Check_Form
import numpy as np
from flask import Flask, render_template, url_for, redirect
from joblib import load

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


# _____SQL DATABASE SECTION_____
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

lr = load('LogisticRegression_model.joblib')
ref = load('ref.joblib')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/check', methods=['GET', 'POST'])
def check():

    form = Check_Form()
    result = ''

    if form.validate_on_submit():
        provider = form.provider.data
        approach = form.approach.data
        material = form.material.data
        x_pred = np.array(ref.loc[(approach, material, provider)])
        result = lr.predict(x_pred.reshape(1, -1))

        if result == 1: return render_template('yes.html')
        else: return render_template('no.html')

    return render_template('check.html', form=form)


@app.route('/about_us')
def about():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run(debug=True)