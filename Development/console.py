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
team5 = Team("Nemo's Allstars", "Mount Wannahockaloogie")
team_repository.save(team5)
team6 = Team("Looney Tunes", "The Looney Bin")
team_repository.save(team6)


match1 = Match(team1, 2, 1, team2)
match_repository.save(match1)
match2 = Match(team3, 5, 2, team4)
match_repository.save(match2)
match3 = Match(team4, 2, 0, team1)
match_repository.save(match3)
match4 = Match(team3, 4, 0, team2)
match_repository.save(match4)
match5 = Match(team5, 8, 3, team6)
match_repository.save(match5)
match6 = Match(team2, 1, 4, team5)
match_repository.save(match6)
match7 = Match(team6, 0, 3, team4)
match_repository.save(match7)
match8 = Match(team1, 3, 1, team3)
match_repository.save(match8)

match_repository.select_all()
team_repository.select_all()

# team1.team_name = "test"
# team_repository.update(team1)

team_repository.select_all()

# pdb.set_trace()