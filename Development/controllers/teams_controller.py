from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

# New Team
# GET '/teams/new'
@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams  = team_repository.select_all()
    return render_template("teams/new.html", all_teams = teams)

# CREATE Team
# POST '/teams'
@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    team_name = request.form['team_name']
    stadium = request.form['stadium']
    match = match_repository.select_match(team_name)
    # team = Team(team_name, stadium, match) ----- NOT SURE IF I NEED THIS AT THE MOMENT, DOESNT MAKE SENSE, PREVIOUS CODE SHOWS
    team_repository.save(team)
    return redirect('/teams')

# SHOW team
# GET '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['GET'])
def show_team(id):
    team = team_repository.select_team(id)
    return render_template('teams/show.html', team=team)

# EDIT 
# GET '/teams/<id>/edit'
@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = team_repository.select_team(id)
    # match = match_repository.select_all()----- NOT SURE IF I NEED THIS AT THE MOMENT, DOESNT MAKE SENSE, PRVIOUS CODE SHOWS
    return render_template('teams/edit.html', team = team)

#  UPDATE
# PUT '/teams/;<id>'
@teams_blueprint.route("/tasks/<id>", methods = ['POST'])
def update_team(id):
    team_name = request.form['team_name']
    stadium = request.form['stadium']
    team = team_repository.select(team_name)
