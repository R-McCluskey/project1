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