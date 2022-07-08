from . import db


class Vote(db.Model):
    name = db.Column(db.String(), primary_key=True)
    vote_choice = db.Column(db.Integer())

