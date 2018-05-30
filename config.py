DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///testes.db'
SQLALCHEMY_DATABASE_URI = 'postgresql://{name}:{password}@localhost/flaskpj'.format(name='postgres',password='postgres')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'DontTellAnyone'

# flask-security
SECURITY_PASSWORD_SALT = 'saltsaltsatl'
SECURITY_PASSWORD_HASH = 'sha512_crypt'