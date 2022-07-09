from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import Vote
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return redirect(url_for('views.home'))


@views.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return redirect('/voting?name='+request.form.get('name'))

    return render_template('index.html')


@views.route('/voting', methods=['GET', 'POST'])
def vote():
    if request.method == "POST":
        name = request.args
        vote_choice = request.form.get('vote_choice')
        name = request.form.get('name')
        new_vote = Vote(name=name, vote_choice=vote_choice)
        db.session.add(new_vote)
        db.session.commit()

        flash('Vote Registered!', category='success')

        return redirect(url_for('views.vote'))

    return render_template('voting.html')
