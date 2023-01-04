#imports
from flask import Flask, render_template

#Create flask object
app = Flask('__name__')

#route for the homepage
@app.route('/')
def index():
    return render_template('home.html')

#route for displaying infomation on a habitat
@app.route('/habitats/<string:habitat>')
def route_info(habitat):
    return render_template('habitat_info.html',habitat=habitat)

#route for displaying infomation on a pokémon
@app.route('/pokemon/<int:dex_num>')
def pokemon_info(dex_num):
    return render_template('pokemon_info.html',dex_num=dex_num)