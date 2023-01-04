#imports
from flask import Flask, render_template
import json

#Create flask object
app = Flask('__name__')
with open('data/habitats.json','r') as file:
    habitat_data = json.load(file)
with open('data/pokemon.json','r') as file:
    pokemon_data = json.load(file)

#route for the homepage
@app.route('/')
def index():
    return render_template('home.html')

#a route for showing a list of all habitats
@app.route('/habitats/')
def habitat_list():
    return render_template('habitat_list.html',habitats=habitat_data.keys())

#route for displaying infomation on a habitat
@app.route('/habitats/<string:habitat>')
def habitat_info(habitat):
    return render_template('habitat_info.html',habitat=habitat,data=habitat_data[habitat])

#a route for showing a list of all pokemon
@app.route('/pokemon/')
def pokemon_list():
    return render_template('pokemon_list.html')

#route for displaying infomation on a pokémon
@app.route('/pokemon/<int:dex_num>')
def pokemon_info(dex_num):
    return render_template('pokemon_info.html',dex_num=dex_num)