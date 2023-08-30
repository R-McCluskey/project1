DROP TABLE if EXISTS matches;
DROP TABLE if EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255),
  stadium VARCHAR(255)
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  team_1 INT REFERENCES teams(id) ON DELETE CASCADE,
  team_2 INT REFERENCES teams(id) ON DELETE CASCADE,
  score_1 INT,
  score_2 INT
);
