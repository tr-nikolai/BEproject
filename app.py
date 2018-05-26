from flask import Flask, render_template, request, abort, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import DataForm


#  config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'DontTellAnyone'
db = SQLAlchemy(app)


#  models
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_data = db.Column(db.String(100), nullable=False)
    place_conutry = db.Column(db.String(100), nullable=False)
    place_city = db.Column(db.String(100), nullable=False)
    slot_servers = db.Column(db.Integer, nullable=False)
    data_tier = db.Column(db.Integer, nullable=False)

    servers = db.relationship('Server', backref='data', cascade='all, delete-orphan', lazy='dynamic') # у серверов обращаться по имени data server = Servers(name='c3p0', data=anthony) где anthony обьект Data

    def __repr__(self):
        return '<data {} id={} >'.format(self.name_data, self.id)


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_server = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    model_server = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    os = db.Column(db.String(100), nullable=False)

    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)



    def __repr__(self):
        return '<server {} id={} >'.format(self.name_server, self.id)


#  view
@app.route('/', methods=['GET'])
def index():
    data = Data.query.all()
    return render_template('index.html', data=data)


@app.route('/data/<id>/edit/', methods=['GET', 'POST'])


@app.route('/data/<id>/edit/', methods=['GET', 'POST'])
def data_edit(id):
    data = Data.query.filter_by(id=id).first()
    if not data:
        abort(404)
    if request.method == 'POST': #  принимаем достаем данные и перерисовываем страницу
        form = DataForm(formdata=request.form, obj=data)
        form.populate_obj(data)
        db.session.commit()
        return redirect(url_for('index'))
    form = DataForm(obj=data)
    return render_template('data_edit.html', form=form)


@app.route('/data/<id>/delete/', methods=['GET', 'POST'])
def data_delete(id):
    data = Data.query.filter_by(id=id).first()
    if not data:
        abort(404)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/data/create', methods=['GET', 'POST'])
def create_data():
    if request.method == 'POST':
        # print(request.form)
        try:
            data = Data(name_data=request.form['name_data'],
                        place_conutry = request.form['place_conutry'],
                        place_city = request.form['place_city'],
                        slot_servers = request.form['slot_servers'],
                        data_tier = request.form['data_tier'])
            db.session.add(data)
            db.session.commit()
        except:
            print('что-то не так')
        return redirect(url_for('index'))
    form = DataForm()
    return render_template('create_data.html', form=form)


@app.route('/servers', methods=['GET'])
def all_servers():
    servers = Server.query.all()
    return render_template('servers.html', servers=servers)


if __name__ == '__main__':
    app.run(debug=True)