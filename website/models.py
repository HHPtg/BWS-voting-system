from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class HeadBoy(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HeadGirl(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHeadBoy(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHeadGirl(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class SportsCaptain(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceSportsCaptain(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class CulturalHead(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceCulturalHead(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainSpartans(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainSpartans(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainKnights(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainKnights(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainTrojans(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainTrojans(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainSamurais(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainSamurais(db.Model):
    name = db.Column(db.String(), primary_key=True)
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)