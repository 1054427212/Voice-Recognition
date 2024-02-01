from exts import db


class Encoder(db.Model):
    __tablename__ = 'encoder'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    time = db.Column(db.String(255))
    length = db.Column(db.String(255))
    type = db.Column(db.String(255))
    path = db.Column(db.String(255))
