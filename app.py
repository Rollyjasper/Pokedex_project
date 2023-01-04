#imports
from flask import Flask, render_template

#Create flask object
app = Flask('__name__')

#route for the homepage
@app.route('/')
def index():
    return render_template('home.html')

#a route for showing a list of all habitats
@app.route('/habitats/')
def habitat_list():
    return render_template('habitat_list.html')

#route for displaying infomation on a habitat
@app.route('/habitats/<string:habitat>')
def habitat_info(habitat):
    return render_template('habitat_info.html',habitat=habitat)

#a route for showing a list of all pokemon
@app.route('/pokemon/')
def pokemon_list():
    return render_template('pokemon_list.html')

#route for displaying infomation on a pokémon
@app.route('/pokemon/<int:dex_num>')
def pokemon_info(dex_num):
    return render_template('pokemon_info.html',dex_num=dex_num)