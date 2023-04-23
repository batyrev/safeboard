#!/usr/bin/env python3

from os import path
import connexion
from swagger_server.db import db
from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder

basedir = path.abspath(path.dirname(__file__))
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    path.join(basedir, 'searches.db')

db.init_app(app.app)
with app.app.app_context():
    db.create_all()
    db.session.commit()

def main():
    app.add_api('swagger.yaml',
            arguments={'title': 'Поиск файлов по локальной файловой системе'},
            pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
