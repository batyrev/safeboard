from sqlalchemy.exc import IntegrityError

from swagger_server.__main__ import app
from swagger_server.models.db_models import Path, Search, db


def add_new_path(search_id, path):
    with app.app.app_context():
        path = Path(search_id=search_id, path=path)
        try:
            db.session.add(path)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def add_new_search(search_id):
    with app.app.app_context():
        search = Search(search_id=search_id)
        try:
            db.session.add(search)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def get_paths_by_search_id(search_id):
    with app.app.app_context():
        print(search_id)
        paths_query = db.session.query(Path.path).filter(Path.search_id == search_id).all()
        paths = []
        for path in paths_query:
            paths.append(path.path)
        return paths
