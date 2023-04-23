from swagger_server.db import db


class Search(db.Model):
    __tablename__ = 'searches'

    search_id = db.Column(db.String(32), primary_key=True)
    finished = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def serialize(self):
        return {
            'search_id': self.search_id,
            'finished': self.finished,
            'paths': self.paths,
        }


class Path(db.Model):
    __tablename__ = 'paths'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    search_id = db.Column(db.String(32), nullable=False)
    path = db.Column(db.String, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'search_id': self.search_id,
            'path': self.path,
        }
