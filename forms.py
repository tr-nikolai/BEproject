from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, IntegerField
from wtforms.validators import InputRequired


message = 'Поле не далжно быть пустым'

class DataForm(FlaskForm):
    name_data = StringField(label='имя дата центра', validators=[InputRequired(message)])
    place_conutry = StringField(label='страна', validators=[InputRequired(message)])
    place_city = StringField(label='город', validators=[InputRequired(message)])
    slot_servers = IntegerField(label='кол-во серверных слотов', validators=[InputRequired(message)])
    data_tier = SelectField(label='Уровень', choices=[('1', 1), ('2', 2), ('3', 3)])


class ServerForm(FlaskForm):
    name_server = StringField(label='имя сервера', validators=[InputRequired(message)])
    manufacturer = StringField(label='производитель', validators=[InputRequired(message)])
    model_server = StringField(label='модель', validators=[InputRequired(message)])
    serial_number = StringField(label='серийные номер', validators=[InputRequired(message)])
    os = StringField(label='операционная система', validators=[InputRequired(message)])
    data = IntegerField(label='№ дата центра', validators=[InputRequired(message)])