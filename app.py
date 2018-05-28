from flask import Flask, render_template, request, abort, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import DataForm, ServerForm
from models import *



app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


#  view
@app.route('/', methods=['GET'])
def data():
    radio = request.args.get('radio')
    q = request.args.get('q')
    if q:
        data = Data.query.filter(Data.name_data.contains(q)).all()
    elif radio == 'up':
        data = Data.query.order_by(Data.slot_servers).all()
    elif radio == 'down':
        data = Data.query.order_by(Data.slot_servers).all()[::-1]
    else:
        data = Data.query.all()
    return render_template('data.html', data=data)


@app.route('/data/<id>/edit/', methods=['GET', 'POST'])


@app.route('/data/<id>/edit/', methods=['GET', 'POST'])
def data_edit(id):
    data = Data.query.filter_by(id=id).first()
    if not data:
        abort(404)
    if request.method == 'POST':
        form = DataForm(formdata=request.form, obj=data)
        form.populate_obj(data)
        db.session.commit()
        return redirect(url_for('data'))
    form = DataForm(obj=data)
    return render_template('data_edit.html', form=form)


@app.route('/data/<id>/delete/', methods=['GET', 'POST'])
def data_delete(id):
    data = Data.query.filter_by(id=id).first()
    if not data:
        abort(404)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('data'))


@app.route('/data/create', methods=['GET', 'POST'])
def create_data():
    if request.method == 'POST':
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
        return redirect(url_for('data'))
    form = DataForm()
    return render_template('create_data.html', form=form)


@app.route('/servers', methods=['GET'])
def all_servers():
    radio = request.args.get('radio')
    if radio == 'name':
        servers = Server.query.order_by(Server.name_server).all()
    elif radio == 'manufac':
        servers = Server.query.order_by(Server.manufacturer).all()
    else:
        servers = Server.query.all()
    return render_template('servers.html', servers=servers)


@app.route('/servers/<id>/delete', methods=['GET'])
def server_delete(id):
    server = Server.query.filter_by(id=id).first()
    if not server:
        abort(404)
    db.session.delete(server)
    db.session.commit()
    return redirect(url_for('servers_data', id=server.data_id))


@app.route('/servers/<id>', methods=['GET'])
def servers_data(id):
    servers = Server.query.filter_by(data_id=id)
    radio = request.args.get('radio')
    # print(servers.order_by(Server.name_server).all())
    if radio == 'name':
        servers = servers.order_by(Server.name_server).all()
    elif radio == 'manufac':
        servers = servers.order_by(Server.manufacturer).all()
    return render_template('servers.html', servers=servers)


@app.route('/server/create', methods=['GET', 'POST'])
def create_server():
    if request.method == 'POST':
        try:
            data = Data.query.filter_by(id=request.form['data']).all()[0]
        except:
            info = 'Нет такого Дата центра'
            return render_template('teh_info.html', info = info)
        server = Server(name_server =  request.form['name_server'],
                        manufacturer = request.form['manufacturer'],
                        model_server = request.form['model_server'],
                        serial_number = request.form['serial_number'],
                        os = request.form['os'],
                        data = data)
        db.session.add(server)
        db.session.commit()
        return redirect(url_for('all_servers'))
    form = ServerForm()
    return render_template('create_server.html', form=form)


@app.route('/server/<id>/edit/', methods=['GET', 'POST'])
def server_edit(id):
    server = Server.query.filter_by(id=id).first()
    if not server:
        abort(404)
    if request.method == 'POST':
        try:
            data = Data.query.filter_by(id=request.form['data']).all()[0]
        except IndexError:
            info = 'Нет такого Дата центра'
            return render_template('teh_info.html', info=info)

        server.name_server = request.form['name_server']
        server.manufacturer = request.form['manufacturer']
        server.model_server = request.form['model_server']
        server.serial_number = request.form['serial_number']
        server.os = request.form['os']
        server.data = data
        db.session.commit()
        return redirect(url_for('all_servers'))
    form = ServerForm(obj=server)
    return render_template('server_edit.html', form=form)


if __name__ == '__main__':
    app.run()