import pdb 
from models.team import Team
from models.match import Match

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

match_repository.delete_all()
team_repository.delete_all()

team1 = Team("Big Belly Boys", "Grub Arena")
team_repository.save(team1)
team2 = Team("Gladiators", "The Colliseum")
team_repository.save(team2)
team3 = Team("Bahama Mamas", "Paradise Stadium")
team_repository.save(team3)
team4 = Team("G38 Geeks", "The Library")
team_repository.save(team4)

match1 = Match(team1, 2, 1, team2)
match_repository.save(match1)
match2 = Match(team3, 5, 2, team4)
match_repository.save(match2)
match3 = Match(team4, 2, 0, team1)
match_repository.save(match3)
match4 = Match(team3, 4, 0, team2)
match_repository.save(match4)

match_repository.select_all()
team_repository.select_all()

# team1.team_name = "test"
# team_repository.update(team1)

team_repository.select_all()

# pdb.set_trace()