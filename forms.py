from wtforms import Form, StringField, SelectField,IntegerField
from wtforms.validators import Required, InputRequired, DataRequired

class DataForm(Form):
    name_data = StringField(label='имя дата центра', validators=[DataRequired()])
    place_conutry = StringField(label='страна')
    place_city = StringField(label='город')
    slot_servers = IntegerField(label='кол-во серверных слотов')
    data_tier = SelectField(label='Уровень', choices=[('1', 1),('2',2),('3',3)])