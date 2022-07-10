from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import HeadBoy, HeadGirl, ViceHeadBoy, ViceHeadGirl, SportsCaptain, ViceSportsCaptain, CulturalHead, \
    ViceCulturalHead, HouseCaptainSpartans, ViceHouseCaptainSpartans, HouseCaptainKnights, ViceHouseCaptainKnights, \
    ViceHouseCaptainTrojans, HouseCaptainTrojans, HouseCaptainSamurais, ViceHouseCaptainSamurais, User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .staticdata import *

views = Blueprint('views', __name__)


@views.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    if not current_user.username == 'adminacc':
        return redirect(url_for('views.home'))

    keys = CANDIDATES_POSTS.keys()

    data = {}

    for post in keys:
        d1 = {}
        for candidate in CANDIDATES_POSTS[post]:
            result = db.engine.execute(
                f"SELECT COUNT(*) FROM {post} WHERE vote_choice == '{candidate}'"
            )
            d1[candidate] = list(result)[0][0]
        data[post] = d1

    return render_template('admin.html', data=data, keys=keys)


@views.route('/api/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.authorize'))


@views.route('/authorize', methods=['GET', 'POST'])
def authorize():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                flash("Login Successful", category="success")
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash("Login Failed", category='error')

        else:
            flash("Account Doesn't Exist", category='error')

    return render_template('auth.html', user=current_user)


@views.route('/')
@login_required
def index():
    return redirect(url_for('views.home'))


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        return redirect('/voting/' + POSTS[0].replace('_', '-') + '?name=' + request.form.get('name'))

    return render_template('index.html')


@views.route('/voting/<post>', methods=['GET', 'POST'])
@login_required
def vote(post):
    if request.method == "POST":
        name = request.args.get('name')

        if post == "head-boy":
            new_vote = HeadBoy(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "head-girl":
            new_vote = HeadGirl(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-head-boy":
            new_vote = ViceHeadBoy(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-head-girl":
            new_vote = ViceHeadGirl(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "sports-captain":
            new_vote = SportsCaptain(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-sports-captain":
            new_vote = ViceSportsCaptain(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "cultural-head":
            new_vote = CulturalHead(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-cultural-head":
            new_vote = ViceCulturalHead(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "house-captain-spartans":
            new_vote = HouseCaptainSpartans(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-house-captain-spartans":
            new_vote = ViceHouseCaptainSpartans(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "house-captain-samurais":
            new_vote = HouseCaptainSamurais(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-house-captain-samurais":
            new_vote = ViceHouseCaptainSamurais(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "house-captain-knights":
            new_vote = HouseCaptainKnights(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-house-captain-knights":
            new_vote = ViceHouseCaptainKnights(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "house-captain-trojans":
            new_vote = HouseCaptainTrojans(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()
        if post == "vice-house-captain-trojans":
            new_vote = ViceHouseCaptainTrojans(name=name, vote_choice=request.form.get('candidate_select'))
            db.session.add(new_vote)
            db.session.commit()

        if POSTS.index(post.replace('-', '_')) == len(POSTS)-1:
            flash('Vote Registered!', category='success')
            return redirect(url_for('views.thankyou'))
        else:
            print(POSTS[(POSTS.index(post.replace('-', '_')) + 1)].replace('_', '-'))
            return redirect('/voting/' + POSTS[(POSTS.index(post.replace('-', '_')) + 1)].replace('_', '-') + '?name=' + name)

    data = CANDIDATES_POSTS[post.replace('-', '_')]

    post_name = post.replace('-', " ").title()

    print(data)

    return render_template('voting.html', candidates=data, post_name=post_name, length=range(len(data)), imgs=[url_for('static', filename=f'/img/students/{c.lower().replace(" ", "-")}.jpeg') for c in data])


@views.route('/thank-you', methods=["GET"])
@login_required
def thankyou():
    return render_template('thankyou.html')
