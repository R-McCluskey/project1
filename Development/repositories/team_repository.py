from db.run_sql import run_sql

from models.team import Team
from models.match import Match

def save(team):
    sql = "INSERT INTO teams (team_name, stadium) VALUES (%s, %s) RETURNING *"
    values = [team.team_name, team.stadium]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['team_name'], row['stadium'], row['id'])
        teams.append(team)
    return teams

def select_team(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        team = Team(result['team_name'], result['stadium'], result['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)
    
def delete_team(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values =[id]
    run_sql(sql, values)

