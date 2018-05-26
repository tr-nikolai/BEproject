from flask import Flask, render_template, request, abort, url_for
from flask_sqlalchemy import SQLAlchemy


#  config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#  models
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_data = db.Column(db.String(100), nullable=False)
    place_conutry = db.Column(db.String(100), nullable=False)
    place_city = db.Column(db.String(100), nullable=False)
    slot_servers = db.Column(db.Integer, nullable=False)
    data_tier = db.Column(db.Integer, nullable=False)

    servers = db.relationship('Server', backref='data') # у серверов обращаться по имени data server = Servers(name='c3p0', data=anthony) где anthony обьект Data

    def __repr__(self):
        return '<data {} id = {} >'.format(self.name_data, self.id)


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_server = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    model_server = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    os = db.Column(db.String(100), nullable=False)

    data_id = db.Column(db.Integer, db.ForeignKey('data.id'))


    def __repr__(self):
        return '<server {} >'.format(self.name_server)

#  view
@app.route('/', methods=['GET'])
def index():
    data = Data.query.all()
    return render_template('index.html', data=data)


@app.route('/data/<id>/edit/', methods=['GET', 'POST'])
def data_edit(id):
    data = Data.query.filter_by(id=id).first()
    if not data:
        abort(404)
    if request.method == 'POST': #  принимаем достаем данные и перерисовываем страницу
        data.name_data = request.form['name_data']
        print(request.form)
        db.session.commit()
        return render_template('data_edit.html', data=data)
    return render_template('data_edit.html', data=data)


@app.route('/data/create', methods=['GET', 'POST'])
def data_create():   #  создание дата центра
    return None




if __name__ == '__main__':
    app.run(debug=True)