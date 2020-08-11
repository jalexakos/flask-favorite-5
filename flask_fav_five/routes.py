from flask_fav_five import app
from flask import render_template

# Home route
@app.route('/')
def home_page():
    return render_template('home_page.html',methods=['GET','POST'])

# Favorite Five route
@app.route('/fav-five')
def fave_five():
    return render_template('fave-five.html',methods=['GET','POST'])