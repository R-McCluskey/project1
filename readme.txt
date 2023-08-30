BRIEF --

Sports fans have requested an app to be able to follow their favourite football teams and be able to keep track of the league, to be able to view matches, who won, what the score was, upcoming games.

-----------
MVP 
* App should allow the user to create, edit, remove teams in the league. 
* App should allow the user to create new games/matches that will be played.
*The app should be able to display all the games for a team they are included in, as well as all teams that are involved in a game.  
*The app should display each match, as well as the result of a match.

----------------
Extension
* Create a league table, to be able to show the teams, and their position in the table.  


-----------------
Extended Extension
* Teams have players that can be inspected, and potentially see their stats, their game form. 








----------------------------
SETUP

1) Create a database - Database name is sports_league
2) psql -d sports_league -f sports_league.sql   -  This is what you run to test in console. Make sure to drop Database and re-create them if needed (dropdb sports_league, createdb sports_league).
3) 