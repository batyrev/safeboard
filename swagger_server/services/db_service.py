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
        paths_query = db.session.query(Path.path).filter_by(search_id=search_id).all()
        paths = []
        for path in paths_query:
            paths.append(path.path)
        return paths


def get_status_by_search_id(search_id):
    with app.app.app_context():
        finished = db.session.query(Search.finished).filter_by(search_id=search_id).first()
        return finished[0] if finished is not None else None


def set_status_by_search_id(search_id, finished):
    with app.app.app_context():
        try:
            new_search = {"search_id": search_id, "finished": finished}
            db.session.query(Search).filter_by(search_id=search_id).update(new_search)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
