from app import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_data = db.Column(db.String(100), nullable=False)
    place_conutry = db.Column(db.String(100), nullable=False)
    place_city = db.Column(db.String(100), nullable=False)
    slot_servers = db.Column(db.Integer, nullable=False)
    data_tier = db.Column(db.Integer, nullable=False)

    servers = db.relationship('Server', backref='data', cascade='all, delete-orphan', lazy='dynamic')

    def __repr__(self):
        return  str(self.id)


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