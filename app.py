#imports
from flask import Flask, render_template
import json

#Create flask object
app = Flask('__name__')

#load the data from json files
#we do this here to prevent having to load the full json file on page loads
with open('data/habitats.json','r') as file:
    habitat_data = json.load(file)
with open('data/pokemon.json','r') as file:
    pokemon_data = json.load(file)
with open('data/moves.json','r') as file:
    move_data = json.load(file)
with open('data/TMs.json','r') as file:
    tm_data = json.load(file)
with open('data/Tutors.json','r') as file:
    tutor_data = json.load(file)
with open('data/type_colours.json','r') as file:
    type_colours = json.load(file)

#route for the homepage
@app.route('/')
def index():
    return render_template(
        'home.html'
    )

#a route for showing a list of all habitats
@app.route('/habitats/')
def habitat_list():
    return render_template(
        'habitat_list.html',
        habitats=habitat_data.keys()
    )

#route for displaying infomation on a habitat
@app.route('/habitats/<string:habitat>')
def habitat_info(habitat):
    return render_template(
        'habitat_info.html',
        habitat=habitat,
        data=habitat_data[habitat],
        pokemon_data=pokemon_data
    )

#a route for showing a list of all pokemon
@app.route('/pokemon/')
def pokemon_list():
    return render_template(
        'pokemon_list.html',
        pokemon_data=pokemon_data
    )

#route for displaying infomation on a pokémon
@app.route('/pokemon/<int:dex_num>')
def pokemon_info(dex_num):
    pkm = pokemon_data[str(dex_num)]
    pri_col = type_colours[pkm['Type'][0]]['Primary']
    bgd_col = type_colours[pkm['Type'][0]]['Background']
    if len(pkm['Type']) == 1:
        sec_col = type_colours[pkm['Type'][0]]['Secondary']
    else:
        sec_col = type_colours[pkm['Type'][1]]['Secondary']

    return render_template(
        'pokemon_info.html',
        dex_num=dex_num,
        pokemon_data=pkm,
        moves=move_data,
        tm_links=tm_data,
        tutor_moves=tutor_data,
        primary_colour=pri_col,
        seconday_colour=sec_col,
        background_colour=bgd_col,
        stat_colours=[
            "#FF5959",
            '#F5AC78',
            '#FAE078',
            '#9DB7F5',
            '#A7DB8D',
            '#FA92B2',
            bgd_col
        ],
        type_colours=type_colours
    )