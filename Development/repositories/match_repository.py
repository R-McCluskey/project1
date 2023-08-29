import pdb
from db.run_sql import run_sql

from models.match import Match
from models.team import Team

def save(match):
    # pdb.set_trace()
    sql = "INSERT INTO matches (team_1, score_1, score_2, team_2) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [match.team_1.id, match.score_1, match.score_2, match.team_2.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    match.id = id
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        match = Match(row['team_1'], row['score_1'], row['score_2'], row['team_2'], row['id'])
        matches.append(match)
    return matches

def select_match(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        match = Match(result['team_1'], result['score_1'], result['score_2'], result['team_2'], result['id'])
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete_match(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(match):
    sql = "UPDATE matches SET (team_1, score_1, score_2, team_2) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.team_1, match.score_1, match.score_2, match.team_2, match.id]
    run_sql(sql, values)