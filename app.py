from flask import Flask, render_template, request
import dm_data as dd
from dm_app import Dm_App
import random
from wtforms import Form, IntegerField, SubmitField, validators, RadioField
from forms import DiceForm, CityForm

app = Flask(__name__)
app.config['SECRET KEY'] = '123456789'
npc_array = ['Name','Appearance','Race','Gender','Skill','Talent','Mannerism','Ideals','Flaw']
dm = Dm_App()

app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html',title='About')

@app.route('/dm/')
def dm_tools():
    return render_template("dm.html",title='DM Tools')

@app.route('/projects/')
def projects():
    return render_template('projects.html',title='Projects')

@app.route('/dm/npc/')
def npc():
    npc= dm.gen_npc()
    return render_template('npc.html',template_npc=npc, title='DM Tools - NPC')

@app.route('/dm/tavern/')
def tavern():
    tavern = dm.gen_tavern()
    return render_template("tavern.html",tavern=tavern, title='DM Tools - Tavern' )

@app.route('/dm/names/')
def names():
    names = []
    for x in range(10):
            names.append(dm.gen_name())
    return render_template("names.html", names=names, title='DM Tools - Name')

@app.route('/dm/roll/',methods=['GET','POST'])
def rolling():
    roll_dice = '0'
    dice_form = DiceForm(request.form)
    if request.method == 'POST':
        roll_dice = dm.roll_dice(dice_form.dice_type.data,dice_form.rolls.data)
    return render_template("roll.html",dice_form=dice_form,roll_dice=roll_dice, title='DM Tools - Roll')

@app.route('/dm/city/', methods=['GET','POST'])
def city():
    city_ = ''
    city_form = CityForm(request.form)
    if request.method == 'POST':
        city_ = dm.gen_city(city_form.city_size.data,1)
        return render_template('city.html',city_form=city_form,city_=city_)
    else:
        return render_template('cityform.html',city_form=city_form, title='DM Tools - City')

@app.route('/dm/shop/')
def shop():
    gen_shop = dm.gen_shops(1)
    print(gen_shop)
    return render_template('shop.html',gen_shop=gen_shop,npc_array=npc_array, title='DM Tools - Shop')

@app.route('/dm/idea/')
def idea():
    gen_idea = dm.gen_idea(3)
    return render_template('idea.html',idea=gen_idea, title='DM Tools - Idea')

@app.route('/dm/poi')
def poi():
    gen_poi = dm.gen_poi(5)
    return render_template('poi.html',pois=gen_poi, title='DM Tools - Poi')

@app.route('/dm/hook/')
def hook():
    gen_hook = dm.gen_hook(5)
    return render_template('hook.html',hooks=gen_hook, title='DM Tools - Hook')

if __name__ == '__main__':
    app.run()
    debug=True
