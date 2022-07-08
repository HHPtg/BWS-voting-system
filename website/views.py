from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import Vote
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return redirect(url_for('views.home'))


@views.route('/home')
def home():
    return render_template('home.html')


@views.route('/admin')
def admin():
    return render_template('admin.html')


@views.route('/vote/<post>', methods=['GET', 'POST'])
def vote(post):
    if request.method == "POST":
        vote_choice = request.form.get('vote_choice')
        name = request.form.get('name')
        new_vote = Vote(name=name, vote_choice=vote_choice)
        db.session.add(new_vote)
        db.session.commit()

        flash('Vote Registered!', category='success')

        return redirect(url_for('views.vote', post=post))

    return render_template('voting.html')
