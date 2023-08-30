import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", all_matches = matches)

# New MAtch
# GET '/matches/new'
@matches_blueprint.route("/matches/new", methods=['GET'])
def new_match():
    teams  = team_repository.select_all()
    return render_template("matches/new.html", all_teams = teams)

# CREATE Match
# POST '/matches'
@matches_blueprint.route("/matches", methods=['POST'])
def create_match():
    team_1 = team_repository.select_team(request.form['team_1'])
    score_1 = request.form['score_1']
    score_2 = request.form['score_2']
    team_2 = team_repository.select_team(request.form['team_2'])
    match = Match(team_1, score_1, score_2, team_2, id)
    match_repository.save(match)
    return redirect('/matches')

# SHOW match
# GET '/matches/<id>'
@matches_blueprint.route("/matches/<id>", methods=['GET'])
def show_match(id):
    match = match_repository.select_match(id)
    return render_template('matches/show.html', match=match)

# EDIT 
# GET '/matches/<id>/edit'
@matches_blueprint.route("/matches/<id>/edit", methods=['GET'])
def edit_match(id):
    match = match_repository.select_match(id)
    # match = match_repository.select_all()----- NOT SURE IF I NEED THIS AT THE MOMENT, DOESNT MAKE SENSE, PRVIOUS CODE SHOWS
    return render_template('matches/edit.html', match = match)

#  UPDATE
# PUT '/matches/;<id>'
@matches_blueprint.route("/matches/<id>", methods = ['POST'])
def update_match(id):
    # pdb.set_trace()
    # team_1_name = request.form['team_1']
    score_1 = request.form['score_1']
    score_2 = request.form['score_2']
    # team_2_name = request.form['team_2']
    match = match_repository.select_match(id)
    # match.team_1.name = team_1_name
    match.score_1 = score_1
    match.score_2 = score_2
    # match.team_2.name = team_2_name
    # team_repository.update(match.team_1)
    # team_repository.update(match.team_2)
    match_repository.update(match)
    return redirect('/matches')

