from wtforms import Form, IntegerField, SubmitField, validators, RadioField

class DiceForm(Form):
    dice_type = IntegerField('Type of Dice?',[validators.DataRequired()])
    rolls = IntegerField('How many dice?',[validators.DataRequired()])
    submit = SubmitField('Roll!')

class CityForm(Form):
    city_size = RadioField('City Size:',choices = [('s','Small'),('m','Medium'),('l','Large')])
    submit = SubmitField('Submit')
