from wtforms import Form, StringField, SelectField, IntegerField


class DataForm(Form):
    name_data = StringField(label='имя дата центра')
    place_conutry = StringField(label='страна')
    place_city = StringField(label='город')
    slot_servers = IntegerField(label='кол-во серверных слотов')
    data_tier = SelectField(label='Уровень', choices=[('1', 1), ('2', 2), ('3', 3)])


class ServerForm(Form):
    name_server = StringField(label='имя сервера')
    manufacturer = StringField(label='производитель')
    model_server = StringField(label='модель')
    serial_number = StringField(label='серийные номер')
    os = StringField(label='операционная система')
    data = StringField(label='№ дата центра')